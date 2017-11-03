import re
from urllib.request import urlopen

def find_urls(text):
    """
    Looks for and returns urls from a string of HTML.
    A url is here assumed to be of the form
        <a href="PROTOCOL://www.HOST.DOMAIN/PATH"></a>
    where PROTOCOL is either http or https, HOST and DOMAIN consists of [a-zA-z0-9~.-] chars,
    and PATH consists of [a-zA-z0-9~./-@] chars. The "www" part of the url is optional, so the
    search-function does not specify that this has to be in the url (if it is, it will be part
    of the HOST string). HOST and DOMAIN have to be at least one char long, while PATH can be
    empty.
    """


    #For "" quotations
    urls = re.findall(r"<a href=\"(https?://[a-zA-z0-9~.-]+.[a-zA-z0-9~.-]+/?[a-zA-z0-9~./-]*)\".*</a>", text)
    
    #For '' quotations
    urls = urls + re.findall(r"<a href=\'(https?://[a-zA-z0-9~.-]+.[a-zA-z0-9~.-]+/?[a-zA-z0-9~./-]*)'.*</a>", text)

    #Beneath is some changes i made when attempting to solve 5.5. It is less strict in the search..
    """
    regex1 = re.compile(r"<a href=\"(https?://[a-zA-z0-9~.-]+.[a-zA-z0-9~.-]+/?[a-zA-z0-9~./-@]*)\"", re.MULTILINE)
    urls = re.findall(regex1, text)

    regex2 = re.compile(r"<a href=\'(https?://[a-zA-z0-9~.-]+.[a-zA-z0-9~.-]+/?[a-zA-z0-9~./-@]*)'", re.MULTILINE)
    urls = urls + re.findall(regex2, text)
    """

    return urls

def find_emails(text):
    """
    Looks for and returns what most likely is email addresses in a (long) string.
    An email-like substring is of the form NAME@SERVER.DOMAIN.
    NAME and SERVER can consist of [a-zA-z0-9#$%&~'\*+-/=?_|{}.]
    DOMAIN can only consist of alphabetical characters and '.', i.e. [a-zA-Z.], but the first and last
    characters have to be alphabetical. It is (logically) assumed that the DOMAIN name cannot be
    shorter than two characters.
    """

    emails = re.findall(r"[a-zA-z0-9#$%&~'\*+-/=?_|{}.]+@[a-zA-z0-9#$%&~'*+-/=?_|{}.]+\.[a-zA-Z][a-zA-z.]*[a-zA-Z]+", text)
    return emails

def all_the_emails(url, depth):
    print(depth)

    url_req = urlopen(url)
    url_read = url_req.read()
    html_string = url_read.decode("utf8")

    emails = find_emails(html_string)
    #print(emails)

    if depth > 0:
        print("Going to next depth")
        urls = find_urls(html_string)
        print(urls)
        for link in urls:
            new_emails = all_the_emails(link, depth-1)
            for new_email in new_emails:
                emails.add(new_email) #To not add same email twice
        depth-=1

    url_req.close()
    return emails



depth = 3 #Number of times all_the_emails will call itself
url = "https://lucidtech.io/"
all_the_emails(url, depth)

