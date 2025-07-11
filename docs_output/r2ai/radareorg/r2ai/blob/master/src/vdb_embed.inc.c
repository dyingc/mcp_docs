# vdb_embed.inc.c

/* r2ai - MIT - Copyright 2024-2025 pancake */

#include <r_util.h>

#define USE_OLLAMA_EMBED 0

// Create a new global DF entry.
static void gtfidf_add(RList *db_tokens, const char *token) {
	RVdbToken *t = R_NEW (RVdbToken);
	t->token = r_str_trim_dup (token);
	t->count = 1;
	r_list_append (db_tokens, t);
}

static RVdbToken *gtfidf_find(RList *db_tokens, const char *token) {
	RListIter *iter;
	RVdbToken *t;
	r_list_foreach (db_tokens, iter, t) {
		if (!strcmp (token, t->token)) {
			return t;
		}
	}
	return NULL;
}

static inline void gtfidf_list(RVdb *db) {
	// show global token frequency
	RListIter *iter;
	RVdbToken *t;
	eprintf ("TotalDocs: %d\n", db->total_docs);
	r_list_foreach (db->tokens, iter, t) {
		eprintf ("TOKEN %d %s\n", t->count, t->token);
	}
}

static bool valid_token(const char *a) {
	if (!strcmp (a, "pancake")) {
		return false;
	}
	if (!strcmp (a, "author")) {
		return false;
	}
	if (!strcmp (a, "radare2")) {
		return false;
	}
	return true;
}

#if USE_OLLAMA_EMBED
// experimental ollama
static void compute_embedding(RVdb *db, const char *text, float *embedding, unsigned int dim) {
	// curl http://localhost:11434/api/embed -d '{ "model": "llama3:latest", "input": "text" }' |jq -r '.embeddings[0]'
	char *json_text = r_str_escape_utf8_for_json (text, -1);
	const char *model = "llama3:latest";
	char *s = r_sys_cmd_strf ("curl http://localhost:11434/api/embed -d '{ \"model\": \"%s\", \"input\": \"%\" }' |jq -r '.embeddings[0]'", model, json_text);
	RList *list = r_str_split_list (s, "\n", 0);
	RListIter *iter;
	const char *vector;
	int i = 0;
	for (i = 0; i < dim; i++) {
		embedding[i] = 0.0f;
	}
	r_list_foreach (list, iter, vector) {
		float f;
		sscanf (vector, "%f", &f);
		if (f) {
			embedding[i % dim] += f;
			i++;
		}
	}
	printf ("--> %s\n", s);
	r_list_free (list);
	free (json_text);
	free (s);
}
#else
static void compute_embedding(RVdb *db, const char *text, float *embedding, unsigned int dim) {
	// gtfidf_list (db);

	// Zero the embedding vector.
	memset (embedding, 0, dim * sizeof (float));

	/* --- Step 1. Tokenize the Document & Build a Local Frequency Table --- */
	// Make a modifiable copy of the text.
	char *buffer = strdup (text);
	if (!buffer) {
		return;
	}
	// We tokenize by whitespace (spaces, tabs, newlines).
	char *saveptr;
	char *token = strtok_r (buffer, " \t\r\n", &saveptr);

	RList *doc_tokens = r_list_newf (token_free);

	while (token) {
		// Search the local list for this token.
		for (char *p = token; *p; p++) {
			if (!isalnum (*p)) {
				*p = ' ';
			} else {
				*p = (char)tolower ((unsigned char)*p);
			}
		}
		r_str_trim (token);
		RVdbToken *found = gtfidf_find (doc_tokens, token);
		if (found) {
			found->count++;
		} else {
			gtfidf_add (doc_tokens, token);
		}
		token = strtok_r (NULL, " \t\r\n", &saveptr);
	}
	free (buffer);
	db->total_docs++;

	/* --- Step 2. Update Global Document Frequencies --- */
	// Here we use the global definition of token_df (do not re-declare it locally).
	RListIter *iter;
	RVdbToken *dt_token;
	r_list_foreach (doc_tokens, iter, dt_token) {
		RVdbToken *t = gtfidf_find (db->tokens, dt_token->token);
		if (t) {
			if (valid_token (dt_token->token)) {
				t->count++;
				t->df += 1.0f;
			}
		} else {
			gtfidf_add (db->tokens, dt_token->token);
		}
	}
	// Increment the total number of documents.

	/* --- Step 3. Compute TF-IDF for Each Token and Update the Embedding --- */
	RVdbToken *dt;
	r_list_foreach (doc_tokens, iter, dt) {
		// Compute term frequency: tf = 1 + log (token_count)
		float tf = 1.0f + log ((float)dt->count);
		RVdbToken *t = gtfidf_find (db->tokens, dt->token);
		float df_value = t ? t->df : 1.0f;
		// Compute inverse document frequency;
		float idf = log (((float)db->total_docs + 1.0f) / ((float)df_value + 1.0f)) + 1.0f;
		float weight = tf * idf;

		const unsigned int hash = r_str_hash (dt->token);
		unsigned int index = hash % dim;
		// Add the TF-IDF weight to the appropriate bucket.
		embedding[index] += weight;
		//		printf ("TOK %x[%d] %s = %f %f = %f\n", hash, index, dt->token, tf, idf, weight);
	}

	r_list_free (doc_tokens);

	/* --- Step 4. L2 Normalize the Embedding --- */
	double norm_sq = 0.0;
	unsigned int i;
	for (i = 0; i < dim; i++) {
		norm_sq += embedding[i] * embedding[i];
	}
	if (norm_sq > 0.0) {
		double norm = sqrt (norm_sq);
		for (i = 0; i < dim; i++) {
			embedding[i] /= norm;
		}
	}
#if 0
	eprintf ("--> ");
	for (i = 0; i < dim; i++) {
		eprintf (" %f", embedding[i]);
	}
	eprintf ("\n");
#endif
}
#endif
