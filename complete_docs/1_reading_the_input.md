At first the learner needs to know some basic things which can be found [here](https://docs.opencv.org/3.1.0/dc/d2e/tutorial_py_image_display.html). The section of "Matplotlib" could be skipped.<br />
Now when the learner knows how to open an image in grayscale format, we should answer one basic quesion.<br />

<b>Why use the grayscale format ? What is the problem with using color images?</b><br />
The above question could be easily answered by performing one simple activity. Open some text document and capture a picture of it. Now convert the image to grayscale format using any image filter. Is the text still readable ? Yes. Now answering the above question, color information is not required to extract text from our input images. So to make the project time and space effiecient, the color information is discarded.<br />

<b>Coming to the second part of the task</b> (<i>of reading the input image</i>):<br />
To make the project dynamic, it would be helpfull to provide the input image by command line. Rather than doing so by editing the source code each time the project is used.<br />
To use the command line arguments in python, <b>sys</b> module is needed (<i> you can install "sys" using [pip](https://packaging.python.org/tutorials/installing-packages/)</i>). Now we will learn how to use these command line arguments.<br />

<b>using the command line arguments</b>:<br />
A list of all command line arguments passed to the program is maintained by "sys". This list is named as "argv".<br />
The first member of the list "sys.argv" is the name of the program itself followed by passed command line arguments passed.<br />
Since only a single argument is passed, sys.argv[1] will be the input image in our case. As the function "cv2.imread()" needs string input, we use "str(cv2.imread())" as our input image name.<br />
(<i>for example, the program is invoked like [this](complete_doc/Screenshot (310).png)</i>) 

  