# Image-Processor-For-Text-Extraction
<b>Aim</b> : The Aim of the project is to develop a image processor whose output could be used by neural networks for text extraction from the input image.<br />
<b>Input</b> : Image with single black text paragraph on white background as shown in [sample](sample_image.jpg)<br />
<b>Output</b> : Bounding rectangle of each character in the input. But for representation purpose the [output](output.jpg) is an binary image with every character highlighted by enclosing it in a white rectangle.<br />
(<i>The bounding rectangle of each character could be fed to a neural network to covert the character from optical to text format</i>)<br />
<b>Language Used</b> : [Python 3.0](https://www.python.org/download/releases/3.0/)<br />
<b>Modules Used</b> : cv2, numpy and sys (<i>you can download these using [pip](https://packaging.python.org/tutorials/installing-packages/)</i>)<br />
<b>Brief algorithm</b>:<br />
1)Read the input image in Grayscale format.<br />
2)Converted the image to binary format.<br />
3)Cropped the image to minimize non-text region.<br />
4)Removed any tilt from the text.<br />
5)Determined the y-indices of the top and the bottom of each line of text (<i>line segmentation</i>).<br />
6)In each line determined the x-indices of the beginning and the end of each character (<i>character segmentation</i>).<br />
7)The bounding rectangle of each character is found by its x-indices and the y-indices of the line containing the character.<br /><br />
<b>Note</b> - People having the required knowledge of Neural Networks are most invited to work together on a complete optical charactor recognition system. Interested developers can contact manthanchauhan913@gmail.com.<br /><br />
To know complete working of the project the reader can refer [docs](complete_docs).<br />
To use this project in any other project the reader can refer to [user mannual](user_mannual).<br />


 
	
