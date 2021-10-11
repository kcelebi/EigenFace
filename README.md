# EigenFace
Recreation of famous EigenFace Computer Vision problem.

The goal of EigenFace is to, given a set of images of people's faces, find the principal components of these images; i.e the fundamental "building blocks". In this case, we want to look for 15 of these "building blocks". With these principal components, we should be able to, ideally, reconstruct any image in the dataset to some degree. If the dataset is representative of human faces, then we should be able to construct "new" faces to some degree of realism.

We can start out with a dataset of images, I used the one provided by [sci-ki](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html). These images are 250x250 pixels and colored. This implies that they exist in 250x250x3 space. We can reduce dimensionality by making these images black and white, reducing it to 250x250, producing the follow example image:

![aaron](https://github.com/kcelebi/EigenFace/mdimg/bnw.png)
