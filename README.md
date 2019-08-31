# Cognitive-Analysis-Using-Neuro-Sensors-Image-Analysis-Machine-Learning-and-Android-Interface
Classroom Cognitive Analysis Using Neuro sensors/ Emotion Recognition


Abstract




This models presents designing an apparatus to record EEG waveform and then compare it to
pre-recorded reading of different mind states using Arduino brain library and Processing IDE to
obtain the result as the emotion of the student. In the proposed method that obtains EEG
waveforms that is mathematical representation of the emotions. Analyzing those emotions, we
can understand the level of concentration of the student in an efficient manner.
The emotions of the person are taken using a face recognition software which notes down
whether the person is 'angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral'. We combine this
along with the data from the waveform to find out the condition of the student at any point of
time.
It doesn’t use any guess work and hence results obtained are reliable and required actions can be
taken on basis of that.


Motivation




In a classroom during teaching studying period, there is a need of analyzing the basic level of
student understanding in order to improve the teaching method for better teaching experience in
class. This model is required so that concentration level of student’s can be monitored in a
systematic manner and after analyzing the “concentration level” proper steps can be taken to
improve it accordingly.



Introduction



The education of students plays a vital role in development of society and so, student learning
experience is a big area of interest. Proper learning or capturing of subjects taught in a class is
majorly based on the states of brain and how students understands the concept taught. There are
already variety of methods which includes Interpreting the facial expression of the student’s,
examining their hand-eye co-ordination and asking them question regarding class activity and
studies. This model concentrates on the brain activity which are the real factual data to analyze
the state of mind to give appropriate result. In the proposed model we will be using Mind Flex
headset with Arduino UNO as hardware to collect input from brain and get the data in the form
of 8 parameters onto Arduino IDE and we will also be using processing IDE for visualizing the
cognitive skills. Also we will be using python to manipulate the data coming from Arduino IDE
and to make the user experience good.
We will be building an emotion classifier of a person using a Convolutional Neural Network in
python using Tensorflow and Keras as the backend architectures. A model is trained using
30,000+ tuples present in the dataset. The accuracy of the classifier is around 67%. We will be
using the haar cascade face detection file for initial face detection.


Related Work



Emotion recognition by speech

Several approaches to recognize emotions from speech have been reported. Most researchers
have used global suprasegmentally/prosodic features as their acoustic cues for emotion
recognition, in which utterance-level statistics are calculated. For example, mean, standard
deviation, maximum, and minimum of pitch contour and energy in the utterances are widely used
features in this regard. Dellaert et al. attempted to classify 4 human emotions by the use of pitchrelated features. They implemented three different classifiers: Maximum Likelihood Bayes
classifier (MLB), Kernel Regression (KR), and K-nearest Neighbors (KNN). Roy and Pentland
classified emotions using a Fisher linear classifier.
The main limitation of those global-level acoustic features is that they cannot describe the
dynamic variation along an utterance. To address this, for example, dynamic variation in emotion
in speech can be traced in spectral changes at a local segmental level, using short-term spectral
features

Emotion recognition by facial expressions


Facial expressions give important clues about emotions. Therefore, several approaches have been
proposed to classify human affective states. The features used are typically based on local spatial 
position or displacement of specific points and regions of the face, unlike the approaches based
on audio, which use global statistics of the acoustic features.
Mase proposed an emotion recognition system that uses the major directions of specific facial
muscles. With 11 windows manually located in the face, the muscle movements were extracted
by the use of optical flow. For classification, K-nearest neighbor rule was used, with an accuracy
of 80% with four emotions: happiness, anger, disgust and surprise. Yacoob et al. proposed a
similar method [22]. Instead of using facial muscle actions, they built a dictionary to convert
motions associated with edge of the mouth, eyes and eyebrows, into a linguistic, perframe, midlevel representation. They classified the six basic emotions by the use of a rule-based system
with 88% of accuracy.


Emotion recognition by bimodal data


Relatively few efforts have focused on implementing emotion recognition systems using both
facial expressions and acoustic information. De Silva et al. proposed a rule-based audio-visual
emotion recognition system, in which the outputs of the unimodal classifiers are fused at the
decision-level. From audio, they used prosodic features, and from video, they used the maximum
distances and velocities between six specific facial points. A similar approach was also presented
by Chen et al., in which the dominant modality, according to the subjective experiments
conducted in, was used to resolve discrepancies between the outputs of mono-modal systems. In
both studies, they concluded that the performance of the system increased when both modalities
were used together.
