## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

1 - We believe that cherry leaves which have powdery mildew have clear signs/ marks which will allow Farky & Foods to differentiate between healthy and unhealthy cherry trees
  * An average image study can validate this by looking at dominant features and comparing the variation between images.

2 - We believe we can predict if a leaf is healthy or not based on images of the leaf to a 97% degree of accuracy
  * Train and valididate a model using Convolutional neural Network (CNN) to achieve a model that achieves the required level of accuracy. 
  * Data will be split into test, train and validation sets to complete this. 

## The rationale to map the business requirements to the Data Visualisations and ML tasks

* **Business Requirement 1**: Visually differentiate a healthy cherry leaf from one with powdery mildew (Data Visualisation).
	* We will display the "mean" and "standard deviation" images for healthy and unhealthy cherry trees.
 	* We will display the difference between an average healthy leaf and an average powdery mildew leaf.
	* We will display an image montage for either a healthy leaf or a powdery mildew leaf.

* **Business Requirement 2**:  Predicting if a cherry leaf is healthy or contains powdery mildew (Classification).
	* We want to predict if a cherry leaf is healthy or contains powdery mildew. 
	* We want to build a binary classifier and generate reports.

## ML Business Case

* The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

* To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

* We will need an ML model to predict if a cherry leaf has powdery mildew or not, based on historical image data. It is a supervised model, a 2-class, single-label, classification model.

* Our desired outcome is to provide Farmy & Foods with a more efficient method for detecting powdery mildew on cherry leaves.

* The model success metrics are:
   * We agreed with the client that 97% accuracy would be our target for success.

* The model output is defined as a flag, indicating if the cherry leaf has powdery mildew or not and the associated probability of having mildew or not. The plantation staff will upload the picture to the App. The prediction is made on the fly (not in batches).

* The training data to fit the model has been provided by the client. Over 4000 images taken of their crop fields.
   * Train data - target: has mildew or not; features: all images.

## Dashboard Design

### Page 1: Quick Project Summary
* Quick project summary
	* General Information
		* Powdery mildew is a fungal disease that affects many plant species. 
		* An employee takes a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.
	* Project Dataset.
		* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew.
	* Business requirements
		* The company is concerned about supplying the market with a compromised quality product.
		*  The company needs a faster more scalable option to check its thousands of trees. A ML system to detect an infected leaf would speed up the process

### Page 2: Leaf Visualizer
* It will answer business requirement 1
	* Checkbox 1 - Difference between average and variability image
	* Checkbox 2 - Differences between average healthy and average infected leaf
	* Checkbox 3 - Image Montage

### Page 3: Powdery Mildew detector
* Business requirement 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
* Link to download a set of infected and uninfected leaf images for live prediction.
* User Interface with a file uploader widget. The user should upload multiple leaf images. It will display the image and a prediction statement, indicating if the leaf is infected or not with powdery mildew and the probability associated with this statement. 
* Table with the image name and prediction results.
* Download button to download table.

### Page 4: Project Hypothesis and Validation
* We believe that cherry leaves which have powdery mildew have clear signs/ marks which will allow Farky & Foods to differentiate between healthy and unhealthy cherry trees
  * An average image study can help to investigate it

### Page 5: ML Performance Metrics
* Label Frequencies for Train, Validation and Test Sets
* Model History - Accuracy and Losses
* Model evaluation result

## Testing

Manual Testing was used to test the functionality of the steamlit site:

- Each page opens correctly
- All buttons on each page navigates correctly and takes the user to the correct page
- All buttons on the Leaf Visualiser page works, displaying the correct information when clicked on, then hides the information when clicked on again
- The image montage correctly displays either healthy or unhealthy leaves depending on what the user clicks
- User can upload an image with no issues
- The detector correctly displays whether the leaf is healthy or not, and provides a probabality with this
- The analysis report correctly displays 
- The page is still viewable on different screen sizes

## Unfixed Bugs

- First bug was with deployment. I have had to change the heroku stack from 22 to 20 in order to support python 3.8.12
- Second bug was with deployment. I have had to mannualy delete some img files from the validation input set for the image montage, this was beacause heroku slug size is 500 max. With out manualy deleteing these files it would not deploy. i used tutor support but was not sourced any working solution, this was my only working option i could find as i tried other methods like a .slugignore file and cache purge.

## Deployment

### Heroku

- The App live link is: https://YOUR_APP_NAME.herokuapp.com/
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people that provided support throughout this project.
