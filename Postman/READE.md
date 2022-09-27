# Postman setup 

# Creating a new workspace

**Create a new workspace**

- select **Workspaces** in the header, then select **Create Workspace**
- Name: **BlockChainSentry**
- Summary: **This workspace is created for BlockChainSentry team.**
- Visibility: choose **Team**
- Choose **Create Workspace**

**Managing workspace roles**

- To change the role of people in a workspace, or to remove someone from a workspace
  - Select **Workspaces** and then select **BlockChainSentry**
  - select **Workspace Settings**
  - Select a different workspace **Role** for a person or group:
    - **Admin** - Can manage workspace resources and settings.
    - **Editor** - Can create and edit workspace resources.
    - **Viewer** - Can view, fork, and export workspace resources.
    - **Remove** - Removes the person from the workspace. You can `invite the user` again in the future.

**Moving elements to workspaces**

- Select **Collections, APIs, Environments**  in the sidebar
- Select the **more actions** icon and then select **Move**. 
- Select the **workspace** where you want to move the element, and then select **Move**

**Sharing workspaces**

- Choose **Invite** in the upper-right corner
- Name, email, or group name: **email-address@email.com**
- Choose **Role**
- Click on **Send Invites**

**Deleting a workspace**

- Select **Workspaces**
- On the workspace's **Overview** tab, select **Workspace Settings**
- Select **Delete Workspace**

# Collaboration

## Using version control

### Forking Postman entities
**Creating a fork**

- Select the element in the sidebar
- Select **more actions icon** and choose **Create a Fork**
- Fork label: **give-meaning full name**
- Workspace: Select a workspace where you want to fork
- Select **Fork Collection**

**Viewing fork information**

- Select the **Collection name**
- Select the **fork icon** in the context bar.

## Creating pull requests

**Creating public pull requests**

- Hover over the element in the sidebar
- Select the **more actions icon**
- Select **Create pull request**

**Pull request settings**

## Watching a pull request

## Reviewing pull requests

**Viewing the diff**

**Adding comments**

**Editing or declining a pull request**

**Approving a pull request**

**Pulling updates**

**Merging changes**

# Create environments

**Create a new environment**

- select **Environments** on the left and select **+**
- Mouse over on **New Environment** and click on **View more actions** (...)
- Choose **rename** give name as **prod_environment**
- Add **url** variable
  - Click on **Add a new variable** and give name as **url**
  - Choose TYPE as **default**
  - INITIAL VALUE : **https://bcs-scanner-v2.blockchainsentry.com**
  - CURRENT VALUE : **https://bcs-scanner-v2.blockchainsentry.com**
  - Click on **Save** to Save environment 
- Add **cognito-user-id** variable
  - Click on **Add a new variable** and give name as **cognito-user-id**
  - Choose TYPE as **default**
  - INITIAL VALUE : **cognito-user-id-goes-here**
  - CURRENT VALUE : **cognito-user-id-goes-here**
  - Click on **Save** to Save environment

**Export Environment variables**

- select **Environments** on the left navigation 
- Choose **prod_environment**
- Click on **View more actions** at top right side corner
- Choose **Export**
- Choose Location in local workstation and click on **Save**

# GitHub Integration

**Generating a GitHub personal access token**

1. Sign in to `GitHub`
2. Click on **profile** and choose **Settings**
3. Scroll down and choose **Developer settings**
4. Choose **Personal access token**
5. Click on **Generate new token**
6. Enter the password for the confirmation and Sign IN
7. Note: **postman**
8. Expiration: choose **No expiration**
9. Select the **repo** and the user **scopes**
10. Click on **Generate token**
11. Copy the token and save it safely.

**Backing up collections on GitHub**

1. From the **Home** page select **Integrations**
2. Search and select **GitHub**
3. Next to **Backup a collection**, select **Add Integration**
4. Enter your GitHub **Personal Access Token** and select **Authenticate and Proceed**
5. Nickname: **example**
6. Choose workspace: **Choose your workspace**
7. Choose Collection: choose collection which you want to backup.
8. Choose Repository: 
9. Enter Directory (optional):
10. Enter filename:
11. Choose Branch: **main**
12. Choose **Add Integration**

**Import collections from GitHub**

1. From the **Home** page select **Your workspace**
2. Choose **import**
3. Choose **Code repository**
4. Select **GitHub**
5. Choose **Grant** in the browser.
6. Choose **Authorize postmanlabs**
7. Select your GitHub organization: Choose the **organization**
8. Select repository: Choose the **repository**
9.  Select branch: **main**
10. Choose **Continue**
11. Choose **Import**

**Change Working directory**

- Choose **Settings** gear icon
- Under **Working directory** 
- Set **Location** to **~/Postman/files**
- Click on the **x** to close
