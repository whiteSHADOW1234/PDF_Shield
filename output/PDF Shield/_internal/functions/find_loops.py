# Complete function of the recursion infinite loop detection
import re
import networkx as nx
import matplotlib.pyplot as plt
import subprocess

import matplotlib
matplotlib.use('SVG')

# import matplotlib
# matplotlib.use('agg')

def extract_child_objects(input_text):
    pattern = re.compile(r'(\d+ \d+ R)')
    matches = pattern.findall(input_text)
    return matches

def generate_regex(input_string):
    escaped_input = re.escape(input_string)
    regex_pattern = r"endobj(?:(?!endobj).)*?" + escaped_input + r".*?endobj"
    regex = re.compile(regex_pattern, re.DOTALL)
    return regex

def find_loops(pdf_path, root):
    # Read the PDF file as binary
    with open(pdf_path, 'rb') as pdf_file:
        # Read all bytes from the PDF
        pdf_bytes = pdf_file.read()

    # Decode the bytes with UTF-8 encoding and print as a string
    decoded_pdf_text = pdf_bytes.decode('utf-8', errors='ignore')  # 'ignore' handles non-UTF-8 bytes

    page_num = 0

    pages = []

    # Create a directed graph
    G = nx.DiGraph()

    self_recursion = False

    # Use regular expressions to find the block contains
    pattern = re.compile(r'(?:\d+ \d+ obj|(?:\/Pages|\/OpenAction|\/Next|\/Kids|\/Extends|\/First|\/AA<<\/O|\/Contents)\s?\[?[\d+ \d+ R]+\]?)')
    matches = pattern.findall(decoded_pdf_text)

    if matches:
        print("---MATCHES---")
        print(matches)


        for item in matches:
            if item[0] == '/':
                if "/Kids" in item:
                    print("Found Kids")
                    print(item)
                    child = extract_child_objects(item)
                    for i in child:
                        print(i)
                        pages.append(i.split()[0])
                    print(f"Current Page Objects: {pages}")


                child = extract_child_objects(item)
                for i in child:
                    print(i)
                    G.add_edge(current_num, i.split()[0])
                            
            else:
                current_num = item.split()[0]
                current_gen = item.split()[1]
                dynamic_regex = generate_regex(f"{current_num} {current_gen} obj")
                matches = dynamic_regex.findall(decoded_pdf_text)
                if matches:
                    # Find the number between "/D [" and " /Fit]" by using regular expression
                    find_fit = re.compile(r'(?<=/D\[)\d(?=/Fit\])')
                    print("OBJECTS MATCHES:")
                    print(matches)

                    if matches[0]:
                        fit_matches = find_fit.findall(matches[0])

                    if fit_matches:
                        if fit_matches[0]:
                            print(f"Link to page {fit_matches}")
                            G.add_edge(current_num, pages[int(fit_matches[0])])

                print(item)



        # Check Cycles
        # cycles = list(nx.simple_cycles(G))

        # if cycles:
        #     print("The graph contains cycles.")
        #     print("Cycles:", cycles)
        # else:
        #     print("The graph is acyclic.")

        # Draw the graph (NOT SURE THIS WILL WORK OR NOT)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, font_color='black', font_weight='bold', arrowsize=15)

        # Display the graph
        # plt.show()
        plt.savefig('infinite_object_loop_graph.png')
        plt.close()
        subprocess.Popen(['start', 'infinite_object_loop_graph.png'], shell=True)
        print("End of finding object loops...")

    else:
        print("No infinite loops found in the PDF.")
        pop_window = tk.Toplevel(root)  # Create a new top-level window
        pop_label = tk.Label(pop_window, text="No matching block found in the PDF.")
        pop_label.pack()
        root.withdraw()