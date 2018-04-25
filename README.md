# Image-Processor-For-Text-Extraction
<b>Aim</b> : The Aim of the project is to develop a image processor whose output could be used by neural networks for text extraction from the input image.<br />
<b>Input</b> : Image with single black text paragraph on white background as shown in [sample](sample_image.jpg)<br />
<b>Output</b> : Bounding rectange of each charactor in the input. But for representation purpose the [output](output.jpg) is an binary image with every charactor highlighted by enclosing it in a white rectangle.<br /><br />
<b>Pre-requisites</b> :<br />
	<b>Python</b> - Basic syntax, functions :str(), len(), range(), sum()	 {you can read about these functions [here](https://docs.python.org/3.4/library/functions.html)} and [handling command line arguments in python](http://www.pythonforbeginners.com/argv/more-fun-with-sys-argv).<br />
	<b>OpenCV</b> - imread(), dilate(), findContours(), contourArea(), Canny(), adaptiveThreshold(), erode(), bitwise_and(), minAreaRect(), getRotationMatrix2D(), warpAffine(), rectangle(), resize(), imwrite(), waitKey() and destroyAllWindows{you can read about these functions [here](https://docs.opencv.org/3.1.0/d2/d96/tutorial_py_table_of_contents_imgproc.html)}<br />
	<b>Numpy</b> - ones(), where(), column_stack(){you can read about these functions [here](https://docs.scipy.org/doc/numpy-1.14.0/genindex.html)}<br />
 
	
