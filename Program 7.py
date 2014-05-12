#! /usr/bin/pythonw
##CS 101
##Program 7
##Malcolm Parrish
##mp2gb@mail.umkc.edu)
##
##PROBLEM: Write a Python program for Website analysis.  The program analyzes website files on a disk to find broken and orphaned links.  Also utilizes unit testing to test for proper return values.
##
##ALGORITHM: See separate file

import os


def MakeFullPath(path : str, filename : str) -> str:
    """ combines path and filename for a full filename.  If path does not end in \\ then it appends it

    Arguments : 
    path : str, the path to the file
    filename : str, the name of the file.
    Returns : 
    path concatenated with filename.  
    If path does not end with a backslash, then append one if path has data in it.

    """

    try:                               #check if valid path
        os.path.isdir(path) 
    except IOError:
        print("Please enter a valid directory")

    try:                               #check if valid filename
        os.path.isfile(filename)
    except IOError:
        print("Please enter a valid filename")

    full_filename = path + "/"+ filename
    if full_filename[-1] != os.path.sep:
        full_filename += os.path.sep

    return full_filename




def GetHREFLinks(html_str) -> list:
    """ Takes a string and returns a list of the href values
    Arguments : 
    html_str : str - The html to be processed to find any href="" links.
    Returns : A list of strings that are the links included in the html string.  
    Only the portion after href= and between the quotes
    """
    href_list = []
    end_quote = 0
    i = 0

    while i < len(html_str):
        start = html_str.find("href", end_quote + 1)
        i += 1

        if start != -1:
            start_quote = html_str.find('"', start)
            end_quote = html_str.find('"', start_quote + 1)
            href = html_str[start_quote + 1 : end_quote]
            href_list.append(href)
            
        else: 
            continue

    return href_list




def FileLinkTuples(path : str, filename : str) -> list:
    """Returns a tuple of links from the file 
    Arguments :
    path : str - The path to the filename.  Might be relative path.
    filename : str - The name of the html file to open and analyze.
    Returns : list of tuples.  
    Each tuple has the 4 values. 
    HTMLFile - HTML file and path to the source file the link was found in.
    fulllinkpath - Full path to the link on the system.  Not a relative path.
    linkpath - Path and name to the link specified.  Relative address. 
    file exists - Boolean indicating if the file at the full link path exists.
    Example 
    [ (('sample\\index.html', 'C:\\Website Analysis\\downloads.html', 'downloads.html', True)
    ]

    """

    filelink_list = []
    full_file = os.path.join(path, filename)

    file = open(full_file)
    href_list = GetHREFLinks(file.read())

    for link in href_list:
        
        fulllinkpath = os.path.realpath(link)
        linkpath = os.path.join("sample", link) 
        fileexists = os.path.isfile(fulllinkpath)

        tup = (full_file , fulllinkpath, linkpath, fileexists)
        filelink_list.append(tup)


    return filelink_list





def GetOrphanedLinks(html_list : list, link_list : list) -> list:
    """ Returns the tuples from html_list that are not included in any link in link_list 

    Arguments :
    html_list : list - List of tuples of the source html files that were analyzed.
    ( fullpath, relativepath )
    link_list : list of strings.  The full path links to required resources.
    Returns : List of tuples ( fullpath, relativepath ) of any source html files that
    were not referenced by an href= link.  These are orphaned files that
    a user can't navigate to.

    """

    orphan_list = []

    for tpl in html_list:
        if tpl[0] not in link_list:

            orphan_list.append(tpl)

    return orphan_list





def GetValidDirectory(prompt : str) -> str:
    """ Returns a valid directory entered from the user.

    Arguments :
    prompt : str - The text displayed to the user asking them to enter a directory.
    Returns : String of a valid directory that the user entered.
    Errors  : Displays a warning if the user does not enter a valid directory.
    """

    Again = True
    while Again == True:
        website_path = input(prompt)
        if os.path.isdir(website_path) == True:
            Again = False
        else:
            print("Please enter a valid directory")

    return website_path



def DisplayOrphanedLinks(orphan_list : list):
    """ Displays the orphaned links on a website

    Purpose : Prints the output of orphaned links.
    Arguments : orphan_list is a list of tuples ( fullpath, relativepath )
    Returns : none

    Sample :
    Orphaned links
    sample\aboutus.html
    sample\jobs.html
    """

    print("Orphaned Links:")
    for tpl in orphan_list:
        
        print("{:>10}{}".format("",tpl[1]))


def DisplayBrokenLinks(websitelinks : list):
    """ Displays the broken links on a website

    Purpose : Prints the output of broke links.
    Arguments : websitelinks is a list of tuples ( source, fullpath, relativepath, exists )
    Returns : none

    Sample :
    Broken links
    Source HTML                   Link
    ============================================================
    sample\assignments.html       sample\downloads.html
    sample\index.html             sample\dist\css\missing.css

    """

    print("Broken links")
    print("{} {:>22}".format("Source HTML", "Link"))
    print("="*50)
    for link in websitelinks: 
        if link[3] == False:
            
            print("{:<30} {}".format(link[0], link[2] ))



if __name__ == '__main__':
    website_path = GetValidDirectory("Enter the path to the website : ")

    websitelink_list = []   #List of tuples containing the source link information
    htmlfiles = []          #List of the html files we analyze on the site

    for dirname, subdir_list, file_list in os.walk(website_path):
        for file in file_list:
            #Check the file extension.  Only analyze files that are .html
            filename, fileext = os.path.splitext(file)
            if fileext == ".html":
                relative_file = MakeFullPath(dirname, file)
                full_file = os.path.realpath(relative_file)
                
                htmlfiles.append( (full_file, relative_file) )

                filelinks = FileLinkTuples(dirname, file)
                websitelink_list.extend(filelinks)
    


    #Files that do not have a link to them.
    link_list = [linktuple[1] for linktuple in websitelink_list]
    
    orphan_list = GetOrphanedLinks(htmlfiles, link_list)
    
    DisplayOrphanedLinks(orphan_list)

    print()

    DisplayBrokenLinks(websitelink_list)
