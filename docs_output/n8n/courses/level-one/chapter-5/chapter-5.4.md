# Setting values for processing orders | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/courses/level-one/chapter-5/chapter-5.4.md "Edit this page")

# 4\. Setting Values for Processing Orders#

In this step of the workflow, you will learn how to select and set data before transferring it to Airtable using the Edit Fields (Set) node. After this step, your workflow should look like this:

[View workflow file](/_workflows//courses/level-one/chapter-5/chapter-5.4.json)

The next step in Nathan's workflow is to filter the data to only insert the `employeeName` and `orderID` of all `processing` orders into Airtable.

For this, you need to use the [Edit Fields (Set) node](../../../../integrations/builtin/core-nodes/n8n-nodes-base.set/), which allows you to select and set the data you want to transfer from one node to another.

Edit Fields node

The Edit Fields node can set completely new data as well as overwrite data that already exists. This node is crucial in workflows which expect incoming data from previous nodes, such as when inserting values into spreadsheets or databases.

## Add another node before the Airtable node#

In your workflow, add another node before the **Airtable node** from the **If node** in the same way we did it in the [Filtering Orders](../chapter-5.3/#add-if-node-before-the-airtable-node) lesson on the If node's `true` connector. Feel free to drag the Airtable node further away if your canvas feels crowded.

## Configure the Edit Fields node#

Now search for the **Edit Fields (Set) node** after you've selected the **+** sign coming off the If node's `true` connector.

With the Edit Fields node window open, configure these parameters:

  * Ensure **Mode** is set to **Manual Mapping**.
  * While you can use the **Expression editor** we used in the [Filtering Orders](../chapter-5.3/) lesson, this time, let's drag the fields from the **Input** into the **Fields to Set** :
    * Drag **If** > **orderID** as the first field.
    * Drag **If** > **employeeName** as the second field.
  * Ensure that **Include Other Input Fields** is set to false.

Select **Execute step**. You should see the following results:

![Edit Fields \(Set\) node](/_images/courses/level-one/chapter-five/l1-c5-4-set-node.png)_Edit Fields (Set) node_

## Add data to Airtable#

Next, let's insert these values into Airtable:

  1. Go to your Airtable base.
  2. Add a new table called `processingOrders`.
  3. Replace the existing columns with two new columns:

     * `orderID` (primary field): Number
     * `employeeName`: Single line text

Reminder

If you get stuck, refer to the [Inserting data into Airtable](../chapter-5.2/) lesson.

  4. Delete the three empty rows in the new table.

  5. In n8n, connect the Edit Fields node**connector to the** Airtable node**.
  6. Update the Airtable node configuration to point to the new `processingOrders` table instead of the `orders` table.
  7. Test your Airtable node to be sure it inserts records into the new `processingOrders` table.

At this stage, your workflow should now look like this:

[View workflow file](/_workflows//courses/level-one/chapter-5/chapter-5.4.json)

## What's next?#

**Nathan 🙋** : You've already automated half of my work! Now I still need to calculate the booked orders for my colleagues. Can we automate that as well?

**You 👩‍🔧** : Yes! In the next step, I'll use some JavaScript code in a node to calculate the booked orders.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top