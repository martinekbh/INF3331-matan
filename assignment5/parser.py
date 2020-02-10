import re

def parse_nwodkram(text):
    """
    Convert a nwodkram text to html.
    """
    
    html_text = text #to be returned after parsing

    """
    bold = re.compile(r"\%\w.*?\w\%|\%\w\%") #allow space in middle, but not start and end of phrase
    italic = re.compile(r"\*\w.*?\w\*|\*\w\*") #allow space in middle, but not sart and end of phrase

    #Search for bold and italic text, and hyperlinks
    boldtext = bold.findall(text)
    italictext = italic.findall(text)
    hyperlinks = re.findall(r"\[.+\]\(.+\)", text) #allows anything between the brackets
    """

    #Methods for replacing nwodkram text with html
    def html_bold(s): #return bold text for html
        inner_text = list(s.group(2))
        return "<b>" + "".join(inner_text) + "</b>"

    def html_italic(s): #return italic text for html
        inner_text = list(s.group(2))
        return "<i>" + "".join(inner_text) + "</i>"

    def html_hyperlink(s): #return hyperlinks for html
        link_text = "".join(list(s.group(1)))
        url = "".join(list(s.group(2)))
        if re.match(r"http", url) is None and re.match(r"//", url) is None:
            url = "http://" + url #Prevent link from being a relative URL
        return "<a href=\"" + url + "\">" + link_text + "</a>"

    def html_blockquote(s): #return quotes for html
        quote = list(s.group(1))
        return "<blockquote>" + "".join(quote) + "</blockquote>"

    def html_wikipedia(s): #return wikipedia queries for html
        wpquery = "".join(list(s.group(1)))
        wpquery = re.sub(r" ", r"_", wpquery)
        link_text = "Search for '" + wpquery + "'" + " on Wikipedia"
        return "<a href=\"https://en.wikipedia.org/wiki/" + wpquery + "\">" + "".join(link_text) + "</a>"

    def html_image(s): #return images for html
        imageURL = "".join(list(s.group(1)))
        imageWidth = "".join(list(s.group(2)))
        imageHeight = "".join(list(s.group(3)))
        return "<img src=\"" + imageURL + "\" width=\"" + imageWidth + "\" heigth=\"" + imageHeight + "\">"

    #Substitute for html syntax
    html_text = re.sub(r"\\", "", html_text) #Remove ocurrences of \
    html_text = re.sub(r"<(.+)>\(w=(\d+),h=(\d+)\)", html_image, html_text) #Change image links
    html_text = re.sub(r"(\%)(\w.*?\w|\w)(\%)", html_bold, html_text) #Bold text
    html_text = re.sub(r"(\*)(\w.*?\w|\w)(\*)", html_italic, html_text) #Italic text
    html_text = re.sub(r"\[(.+)\]\((.+)\)", html_hyperlink, html_text) #Hyperlinks
    html_text = re.sub(r">>QUOTELINE(.*)", html_blockquote, html_text) #Quotes
    html_text = re.sub(r"\[wp:(\w.*?\w|\w)\]", html_wikipedia, html_text) #Wikipedia queries

    print(html_text)


    return html_text

sample_input = r"""
    This is some Nwodkram text. Note that *this here* and *it* is in italic, and %these words% and %t% is in bold.
    If you want to write an \* or an equal sign and not have the parser eat them, 
    that's easy -  note that \* this \* is not in italic even though it's between two \*s,
    and \% this \% is not in bold.

    [here](www.google.com) is a hyperlink.
    [here](http://www.google.com) is another.
    [wiki](//en.wikipedia.org/wiki/Main_Page) is also a link.
    [and here](https://www.weird?$|site.weird/path/) is a third with some weird characters.
    Follow it at your own peril.

    Ideally, it would be good if your hyperlinks can contain parentheses and underscores.
    But don't worry too much if some weird combination is ambiguous or results in
    weird stuff.

    >>QUOTELINEThis is a quote. -matan
    Text text text text. [wp:Jacob Bernoulli]. 
    [wp:Alpine Skiing]
    Picture: <calvin-and-hobbes.jpg>(w=360,h=394)
    """

#RUN THIS TO TEST SAMPLE ABOVE
#parse_nwodkram(sample_input)

