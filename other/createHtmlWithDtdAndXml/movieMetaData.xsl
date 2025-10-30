<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="html" encoding="UTF-8"/>
  <xsl:template match="/movieMetaData">
    <html>
      <head>
        <meta charset="UTF-8"/>
        <title>Kino – Programm</title>
        <style>
          body { font-family: sans-serif; margin: 2rem; line-height: 1.5; background: #262621; color: #E9E9E9}
          h1 { margin-bottom: 1rem; }
          .movie { padding: 1rem; border: 1px solid #8A96A6; border-radius: 12px; margin-bottom: 1rem; background: #7289A6}
          .title { font-size: 1.4rem; font-weight: 700; }
          .director { font-size: 1.05rem; font-style: italic; color: #D9D9D9; margin-top: .25rem; }
          .meta { margin-top: .5rem; font-size: .95rem; color: #222; }
          .badge { display: inline-block; padding: .1rem .5rem; border-radius: 999px; background: #4968A6; margin-right: .5rem; color: #FFF }
        </style>
      </head>
      <body>
        <h1>Kino – Programm</h1>
        <xsl:for-each select="movie">
          <xsl:sort select="releaseDate" data-type="text" order="ascending"/>
          <div class="movie" id="{@id}">
            <div class="title">
              <xsl:value-of select="title"/>
            </div>
            <div class="director">
              Regie: <xsl:value-of select="director"/>
            </div>
            <div class="meta">
              <span class="badge">Genre: <xsl:value-of select="genre"/></span>
              <span class="badge">Start: <xsl:value-of select="releaseDate"/></span>
              <span class="badge">Rating: <xsl:value-of select="rating"/></span>
            </div>
          </div>
        </xsl:for-each>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>