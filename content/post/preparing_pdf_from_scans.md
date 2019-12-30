+++
author = "Sushant Srivastava"
date = "2019-12-30"
description = "Creating PDF from Scans of the Document"
draft = false
keywords = ["tips", "pdf", "scans"]
tags = ["tips","pdf"]
title = "How did I create PDF from the Scans sent over By Email"
topics = ["pdf"]
type = "post"
+++
First off, the scanned documents that I received from my email were split into
many documents. Let's square this off right away. Combine multiple pdf documents
into a single document using the pdfunite command like so:

```bash
	pdfunite sample_* single.pdf
```

On Ubuntu the pdfunite command is part of the poppler-utils package. If you
are on Ubuntu, you can install the package using the `apt` command.

```bash
	sudo apt-get install poppler-utils
```

Next up, I wanted to create a bookmarked table of contents for the pdf. Doing this
manually would have taken me a long time. The idea of spending my lazy afternoon
transcribing pdf documents did not, to put it mildly, excite me. My search led me
to tesseract, an OCR program that does a wonderful job of extracting text from
images. 

As soon as you decide to use tesseract, you hit another roadblock.
Tesseract works on `.tiff` format and most of the examples from the documentation
were in tiff format. I used Imagemagick's `convert` command to convert pdf to tiff.
I installed imagemagick and ran the convert command only to find myself in another 
impasse. 

I ran into this problem.
> unable to create temporary file `/some/path` Permission denied @ error/pdf.c/ReadPDFImage/465

On further digging, I realized that the convert command used Ghostscript under the hood. A security update
prevented this access. I fixed it by going through this link:
https://alexvanderbist.com/posts/2018/fixing-imagick-error-unauthorized

I got the document converted to tiff and from there I could extract the
text using Tesseract. Lastly, I had to do manual labor to get the
bookmarks and page number in correct order but extracting the text from
the pdf document gave me a good lead. Lastly, I updated the bookmarks
using the `pdftk` command.

### Summary ###

Here are the steps in short:

1. If you have multiple documents, then combine them using the
   `pdfunite` command.

2. Convert the document in `.tiff` format using the `convert` command
   from Imagemagick.

3. Use the `tesseract` command to generate text from your tiff files.

4. Generate the table of contents using the format support by the
   `pdftk` command. The extracted text will give you some idea.

5. Generate the bookmarks and update the documents using the
   `update_info` subcommand from the `pdftk` command. 

You can also try updating the index of the document now that you have
the text inside it, but that's for later. 
