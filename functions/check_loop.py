# Function to check for infinite loop created by name objects in the PDF
import re
import os
# import networkx as nx
# import matplotlib.pyplot as plt
from functions.directed_graph import DirectedGraph
import traceback

# self_recursion = False

def extract_child_objects(input_text):
    pattern = re.compile(r'(\d+ \d+ R)')
    matches = pattern.findall(input_text)
    return matches

def generate_regex(input_string):
    escaped_input = re.escape(input_string)
    regex_pattern = r"endobj(?:(?!endobj).)*?" + escaped_input + r".*?endobj"
    regex = re.compile(regex_pattern, re.DOTALL)
    return regex




def check_loop(path):
    try:
        page_num = 0

        pages = []

        # Create a directed graph
        # G = nx.DiGraph()
        G = DirectedGraph()

        # Read the PDF file as binary
        with open(path, 'rb') as pdf_file:
            # Read all bytes from the PDF
            pdf_bytes = pdf_file.read()

        # Decode the bytes with UTF-8 encoding and print as a string
        decoded_pdf_text = pdf_bytes.decode('utf-8', errors='ignore')  # 'ignore' handles non-UTF-8 bytes

        # Use regular expressions to find the block
        pattern = re.compile(r'(?:\d+ \d+ obj|(?:\/(?:P|#80)(?:a|#97)(?:g|#103)(?:e|#101)(?:s|#115)|\/(?:O|#79)(?:p|#112)(?:e|#101)(?:n|#110)(?:A|#65)(?:c|#99)(?:t|#116)(?:i|#105)(?:o|#111)(?:n|#110)|\/(?:N|#78)(?:e|#101)(?:x|#120)(?:t|#116)|\/(?:K|#75)(?:i|#105)(?:d|#100)(?:s|#115)|\/(?:E|#69)(?:x|#120)(?:t|#116)(?:e|#101)(?:n|#110)(?:d|#100)(?:s|#115)|\/(?:F|#70)(?:i|#105)(?:r|#114)(?:s|#115)(?:t|#116)|\/(?:A|#65)(?:A|#65)<<\/(?:O|#79)|\/(?:C|#67)(?:o|#111)(?:n|#110)(?:t|#116)(?:e|#101)(?:n|#110)(?:t|#116)(?:s|#115))\s?\[?[\d+ \d+ R]+\]?)')
        matches = pattern.findall(decoded_pdf_text)

        if matches:
            # print("---MATCHES---")
            # print(matches)


            for item in matches:
                # print("CHECKING...")
                if item[0] == '/':
                    kids_pattern = re.compile(r'(?:K|#75)(?:i|#105)(?:d|#100)(?:s|#115)')
                    if kids_pattern.search(item):
                        # print("Found Kids")
                        # print(item)
                        child = extract_child_objects(item)
                        for i in child:
                            # print(i)
                            pages.append(i.split()[0])
                        # print(f"Current Page Objects: {pages}")

                    child = extract_child_objects(item)
                    for i in child:
                        # print(i)
                        G.add_edge(current_num, i.split()[0])
                                
                else:
                    current_num = item.split()[0]
                    current_gen = item.split()[1]
                    dynamic_regex = generate_regex(f"{current_num} {current_gen} obj")
                    matches = dynamic_regex.findall(decoded_pdf_text)
                    if matches:
                        # Find the number between "/D [" and " /Fit]" by using regular expression
                        find_fit = re.compile(r'/(?:D|#68)\[(\d)/(?:F|#70)(?:i|#105)(?:t|#116)\]')
                        if matches[0]:
                            fit_matches = find_fit.findall(matches[0])

                        if fit_matches:
                            if fit_matches[0]:
                                # print(f"Link to page {fit_matches}")
                                G.add_edge(current_num, pages[int(fit_matches[0])])

                    print(item)
            #         print("END CHECKING")
            # print("ABOUT TO CHECK CYCLES")
            # Check Cycles
            # cycles = list(nx.simple_cycles(G))
            cycles = G.has_cycle()
            # print("FINISHED CHECKING CYCLES")

            if cycles:
                print("The graph contains cycles.")
                # print("Cycles:", cycles)
                return True
            else:
                print("The graph is acyclic.")
                return False
        else:
            print("No infinite loop found in the PDF.")
            return False
    except Exception as e:
        print("Error: " + str(e))
        traceback.print_exc()
        return False