![PDF_Shield](https://socialify.git.ci/whiteSHADOW1234/PDF_Shield/image?description=1&descriptionEditable=A%20Python%20tool%20to%20detect%20and%20prevent%20PDF‑based%20DoS%0Aand%20Embedded%20JavaScript%20attacks.&forks=1&issues=1&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPD94bWwgdmVyc2lvbj0iMS4wIj8%2BCjxzdmcgd2lkdGg9IjI4LjgiIGhlaWdodD0iMjguOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczpzdmc9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2Utd2lkdGg9IjAuMDAwMjQwMDAwMDAwMDAwMDAwMDMiPgogPGcgY2xhc3M9ImxheWVyIj4KICA8dGl0bGU%2BTGF5ZXIgMTwvdGl0bGU%2BCiAgPGcgaWQ9IlNWR1JlcG9fdHJhY2VyQ2FycmllciIgc3Ryb2tlPSIjZDg0NjQ2IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMC45NiI%2BCiAgIDxwYXRoIGQ9Im0yLjIyLDEyLjI3YzAsLTQuMzggMCwtNi41NyAwLjUyLC03LjMxYzAuNTIsLTAuNzQgMi41NywtMS40NCA2LjY4LC0yLjg1bDAuNzksLTAuMjdjMi4xNCwtMC43MyAzLjIyLC0xLjA5IDQuMzMsLTEuMDljMS4xMSwwIDIuMTksMC4zNyA0LjMzLDEuMDlsMC43OSwwLjI3YzQuMTEsMS40MSA2LjE3LDIuMTEgNi42OCwyLjg1YzAuNTIsMC43NCAwLjUyLDIuOTMgMC41Miw3LjMxYzAsMC42NiAwLDEuMzcgMCwyLjE1YzAsNy43MiAtNS44LDExLjQ3IC05LjQ0LDEzLjA2Yy0wLjk5LDAuNDIgLTEuNDgsMC42NCAtMi44NywwLjY0Yy0xLjQsMCAtMS44OSwtMC4yMiAtMi44NywtMC42NGMtMy42NCwtMS41OSAtOS40NCwtNS4zNCAtOS40NCwtMTMuMDZjMCwtMC43OCAwLC0xLjQ5IDAsLTIuMTV6IiBmaWxsPSIjZWM0YjRiIiBpZD0ic3ZnXzIiLz4KICA8L2c%2BCiAgPHRleHQgZmlsbD0iI2ZmZmZmZiIgZm9udC1mYW1pbHk9IlNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTAiIGlkPSJzdmdfNCIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjE0LjcxIiB4bWw6c3BhY2U9InByZXNlcnZlIiB5PSIxNy45NSI%2BUERGPC90ZXh0PgogPC9nPgo8L3N2Zz4%3D&name=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Light)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
##  Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Motivation](#motivation)
- [Basic PDF Syntax](#basic-pdf-syntax)
- [Attack](#attack)
- [Defense](#defense)
- [Usage](#usage)
- [References & Relative News](#references-&-relative-news)
- [Contributions](#contributions)

## Introduction 
PDF Shield is a Python-based tool designed to detect and mitigate potential Denial of Service (DoS) attacks and embedded JavaScript threats within PDF files. By analyzing PDF structures, it helps users identify malicious content that could compromise system security.​

## Features
- **Automated PDF Monitoring:** Real-time scan of downloaded PDFs for potential DoS or malicious JavaScript.

- **Drag & Drop:** Standalone executable supports drag-and-drop scanning on Windows.

- **Customizable Alerts:** Pop-up notifications inform of embedded JS, infinite loops, deflate bombs.

- **Extensible:** Easily add new detection rules via a modular plugin architecture.

- **Cross-Browser Defense:** Focused on PDF engines in Chrome, Edge, Brave (PDFium-based). However, our detection methods cover most common risks in PDF.js (Firefox) too.



## Motivation

[PDF attacks, particularly as a method within social engineering attacks, have seen a significant increase in occurrence.](https://gbhackers.com/virustotal-malware-trends/) [Cyber adversaries exploit the flexibility of PDF files, often leveraging JavaScript customization to target unsuspecting users.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/threat-loaded-malicious-pdfs-never-go-out-of-style/) [Despite attempts to address vulnerabilities, built-in PDF reader engines in modern browsers remain vulnerable.](https://github.com/RUB-NDS/PDF101/tree/master/02-exploits/24-chrome-browser) To mitigate risks, the PDF DoS Detector aims to reduce the number of victims by alerting users to potential DoS attack methods found within PDF files.

## Basic PDF Syntax
&nbsp;&nbsp;You can gain valuable insights into PDF syntax by watching this informative video titled <a href="https://www.youtube.com/watch?v=k9g9jZdjRcE&ab_channel=TROOPERSITSecurityConference">TROOPERS15 Ange Albertini and Kurt Pfeifle - Mastering Advanced PDF Techniques.</a>
    
&nbsp;&nbsp;Here is some crucial information in the video that will help you understand what this project is all about:
1. A PDF's body section consists of objects, commencing with `<number> <generation> obj` and concluding with `endobj`.
   ![rJn6sLelp](https://github.com/whiteSHADOW1234/PDF_Sheld/assets/91242001/0aeea65f-1f43-4045-a17e-aa079ec1940d)

3. Here's how object references work:
    ![ByuCTUggT](https://github.com/whiteSHADOW1234/PDF_Sheld/assets/91242001/25b66db6-1b94-4013-82de-36ace47348dc)
   
    ![HklEAUge6](https://github.com/whiteSHADOW1234/PDF_Sheld/assets/91242001/e2dacfa3-91dc-4154-bd61-9c236d0a70f4)

    ![rJlrCUxx6](https://github.com/whiteSHADOW1234/PDF_Sheld/assets/91242001/ce28a80d-543c-4463-aca9-0da144dec32b)

    **NOTED: Name objects begin with a forward slash (`/`), and the letter within can be represented in hexadecimal notation!!!**
5. Here's a breakdown of how objects are parsed:
    ![SkrzWPlxp](https://github.com/whiteSHADOW1234/PDF_Sheld/assets/91242001/48aea2be-2184-4f33-b82c-571c6c118898)

### Use real situation as an example
&nbsp;&nbsp;The information provided above may not be sufficient once we open the `embedded.pdf` file, which will be generated by following the steps outlined in the "Basic Attack Method" section, using a text editor such as VSCode.

&nbsp;&nbsp;You will probably observe two occurrences of `/JavaScript` within the PDF document:
1. The first occurrence of this can be found within an object like the one below, denoting the moment at which the `/JavaScript` object will be run.
    ```pdf
    ...
    3 0 obj
    <<
    /Type /Catalog
    /Pages 1 0 R
    /Names <<
    /JavaScript <<
    /Names [ (41d4efc4\055d000\05546e4\055a973\0556f92c8bbd0f7) 29 0 R ]
    >>
    >>
    >>
    endobj
    ...
    ```
2. The second one will appear prior to the `xref` section, instructing the PDF to execute the subsequent text as JavaScript code. [Here's a more detailed explanation of what it accomplishes.](https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting/pdf-injection)
    ```pdf
    ...
    29 0 obj
    <<
    /Type /Action
    /S /JavaScript
    /JS (\012\040\040\040\040app\056alert\050\042Hello\054\040World\041\042\051\073\012)
    >>
    endobj
    xref  <-- This is the beginning of xref part
    ...
    ```


## Attack
### Attacker Model
- Victim opens malicious PDF document
- Bad things happen (attack-dependent)
- No user interaction required

### Simple Attack Method (PoC)
Take JavaScript embedded attack as example:
1. Run `pip install PyPDF2` in the terminal.
2. Next, use the `.add_js()` method of the `PyPDF2` library to create a Python script:
    ```python
    import PyPDF2
    
    def embed_javascript(pdf_file, js_code):
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_writer = PyPDF2.PdfWriter()
    
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
        pdf_writer.add_js(js_code)
    
        with open('embedded.pdf', "wb") as f:
            pdf_writer.write(f)
    
    javascript_code = '''
    while(1){
        app.alert("Hello, World!");
    }
    '''
    
    pdf_file_path = 'blank.pdf'
    with open(pdf_file_path, 'rb') as pdf_file:
        embed_javascript(pdf_file, javascript_code)

    ```
3. Please ensure that you run the Python file you've recently generated. 

    **Don't forget to update the `FILE_NAME` accordingly!**
4. Open the `embedded.pdf` file in the listed web browsers to verify that they trigger an alert window, confirming the successful execution of the embedded JavaScript code within the PDF.

    A. Microsoft Edge:
        ![S181PIggp](https://github.com/whiteSHADOW1234/PDF_Sheld/assets/91242001/d085871f-c6ef-4a60-b566-2e3a05a55c19)

    B. Google Chrome:
       ![S1nMdLlg6](https://github.com/whiteSHADOW1234/PDF_Sheld/assets/91242001/efa3d0c6-69c6-4ef1-84aa-cc46e45db224)
   
    C. Brave:
      ![SJ97_IeeT](https://github.com/whiteSHADOW1234/PDF_Sheld/assets/91242001/6ccfb595-320e-4cfe-af47-e73da492d515)

## Defense
### Defense Model
- The user downloads a potentially malicious PDF.
- The tool conducts an automated scan on the downloaded PDF, presenting the results through a user-friendly pop-up window.
- The user is empowered to make informed decisions, with options to either eliminate identified vulnerabilities within the PDF or proceed with opening it.

### Defense Targets    
- **Note:** The following chart lists CVE information specifically related to PDFium. While it might apply to other PDF engines, our project focuses on creating a defense tool for current web browsers using PDFium, like Chrome, Brave, and Edge. Examples include **CVE-2023-41257 (Foxit Reader 12.1.2.15356)**, **CVE-2023-38573 (Foxit Reader 12.1.2.15356)**, and **CVE-2022-39016 (PDFtron in M-Files Hubshare before 3.3.10.9)**.

#### JavaScript Related Attacks

| Description                                              | Defence Method                             |                   Related CVEs or Papers                    |
| -------------------------------------------------------- | ------------------------------------------ | ----------------------------------------------------------- |
| JS runs stored XSS payload                               | Notice user there's JS embedded in the PDF |                       CVE-2023-45207                        |
| Remote attackers use JS to cause DOS                     | Notice user there's JS embedded in the PDF |                        CVE-2012-2844                        |
| Execute arbitrary JavaScript code with chrome privileges | Notice user there's JS embedded in the PDF |                        CVE-2013-5598                        |
| XSS created by injected JS                               | Notice user there's JS embedded in the PDF |                        CVE-2007-0045                        |
| Infinite loops caused by JavaScripts                     | Notice user there's JS embedded in the PDF |                        CVE-2007-0104                        |
| Sharing of objects over calls into JavaScript runtime    | Notice user there's JS embedded in the PDF |                        CVE-2019-5772                        |
| Form Modification caused by JavaScripts                  | Notice user there's JS embedded in the PDF | Shadow Attacks: Hiding and Replacing Content in Signed PDFs |

- This project alerts users when it finds JavaScript code for two reasons. Firstly, many attacks are connected to JavaScript, according to Spider Experts. Secondly, creating a responsible PDF doesn't need JavaScript; there are built-in Named Objects that support responsible actions. JavaScript is only necessary if the PDF relies solely on it, for example, detecting keystrokes or playing videos without using YouTube or other online services.

#### Name Object Infinite Loops

| Description                                           |                Defence Method                | CVEs           |
| ----------------------------------------------------- | -------------------------------------------- | -------------- |
| Caused by the Named Object "/Kids"                    | Notice user there's infinite loop in the PDF | CVE-2007-0104  |
| Action loop caused by "/Next"                         | Notice user there's infinite loop in the PDF | CVE-2007-0104  |
| Object streams may extend other "/ObjStms"            | Notice user there's infinite loop in the PDF | CVE-2007-0104  |
| Outline entries ("/Outlines") can refer to each other | Notice user there's infinite loop in the PDF | CVE-2007-0104  |
| Incorrect object lifecycle                            | Notice user there's infinite loop in the PDF | CVE-2018-18336 |
| Incorrect object lifecycle                            | Notice user there's infinite loop in the PDF | CVE-2018-17481 |


#### Deflate Bomb

| Description                                                      | Defence Method                                                    | Related CVEs  |
| ---------------------------------------------------------------- | ----------------------------------------------------------------- | ------------- |
| Heap buffer overflow                                             | Notice user there's a posiblity to have a deflate bomb in the PDF | CVE-2020-6513 |
| PDFium does not properly handle certain out-of-memory conditions | Notice user there's a posiblity to have a deflate bomb in the PDF | CVE-2015-1271 |


## Usage

### I. Clone this repo and Automatically scan any downloaded PDF file
1. `git clone` this repository and don't forgot to run `pip install -r requirements.txt`.
2. Execute the `main.py` file.
3. And now download a PDF file.
4. Sit back, relax, and wait for the scanning process to be completed.

### II. Manually drag-and-drop a PDF file for scanning
1. Download the [`PDF Shield` zipped file](https://github.com/whiteSHADOW1234/PDF_Shield/blob/main/output/PDF%20Shield.zip) located in the `output` directory.
2. Unzip it on your device.
3. Locate the `PDF Shield.exe` in the unzipped folder and right-click on it to `Create a Shortcut` on your Desktop.
4. Drag-and-drop the PDF you want to scan onto the icon.
5. Sit back, relax, and wait for the scanning process to be completed.

### III. Automatically scan any downloaded PDF file
1. Download the [`PDF Shield` zipped file](https://github.com/whiteSHADOW1234/PDF_Shield/blob/main/output/PDF%20Shield.zip) located in the `output` directory.
2. Unzip it on your device.
3. Double-click the `PDF Shield.exe` in the unzipped folder to start the scanning program.
4. Now, download a PDF file.
5. Sit back, relax, and wait for the scanning process to be completed.

## References & Relative News
- [PDF101](https://github.com/angea/PDF101)
- [ [TROOPERS15] Ange Albertini, Kurt Pfeifle - Advanced PDF Tricks ](https://www.youtube.com/watch?v=k9g9jZdjRcE&ab_channel=TROOPERSITSecurityConference)
- [Artifacts for "Portable Document Flaws 101" at Black Hat USA 2020](https://github.com/RUB-NDS/PDF101)
- [CVE searching results for "PDF"](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=PDF)
- [Malicious PDFs | Revealing the Techniques Behind the Attacks](https://www.sentinelone.com/blog/malicious-pdfs-revealing-techniques-behind-attacks/)
- [Common Tactics Used by Threat Actors to Weaponize PDFs](https://cybersecuritynews.com/threat-actors-weaponize-pdfs/)
- [How can I extract a JavaScript from a PDF file with a command line tool?](https://stackoverflow.com/questions/29342542/how-can-i-extract-a-javascript-from-a-pdf-file-with-a-command-line-tool)
- [Threat-Loaded: Malicious PDFs Never Go Out of Style](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/threat-loaded-malicious-pdfs-never-go-out-of-style/)
- [One of the easiest and most powerful ways to customize PDF files is by using JavaScript.](https://helpx.adobe.com/acrobat/using/add-debug-javascript.html)
- [Adobe Reader and Acrobat JavaScript Vulnerabilities](https://www.cisa.gov/news-events/alerts/2009/05/13/adobe-reader-and-acrobat-javascript-vulnerabilities)
- [Hackers Use Weaponized PDF Files to Attack Manufacturing, and Healthcare Organizations](https://cybersecuritynews.com/hackers-use-weaponized-pdf-files-to-attack-organizations/)
- [66% of malware delivered via PDF files in malicious emails: Report](https://ciso.economictimes.indiatimes.com/news/vulnerabilities-exploits/66-of-malware-delivered-via-pdf-files-in-malicious-emails-report/100837365)
- [How to protect yourself from the Adobe Reader PDF JavaScript Vulnerability](https://www.bleepingcomputer.com/forums/t/205515/how-to-protect-yourself-from-the-adobe-reader-pdf-javascript-vulnerability/)
- [PDFium](https://pdfium.googlesource.com/pdfium/)
- [Portable-Document-Flaws-101](https://paper.bobylive.com/Meeting_Papers/BlackHat/USA-2020/us-20-Mueller-Portable-Document-Flaws-101.pdf)

## Contributions
Contributions to the PDF DoS Detector are welcome. Whether it's bug fixes, feature enhancements, or other improvements, feel free to contribute to make the tool more effective in protecting users from PDF-based DoS attacks.

Stay secure, and happy browsing!
