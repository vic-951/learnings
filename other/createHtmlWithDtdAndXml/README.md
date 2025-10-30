# Description
In this folder, I created a DTD File to check an XML-structure. Also I created the XML and XSLT-stylesheet to create a static HTML-file with movies.

to render a html file, I used `xsltproc`

with this command you can render your changes
```cli
xsltproc movieMetaData.xsl movieMetaData.xml > movieMetaData.html
```