
#!/usr/bin/env python

from __future__ import print_function

import xml.etree.ElementTree as xml
import argparse
import os



pom_file_name = "pom.xml"
build_file_name = "BUILD"

class pom_2_pants:
    """
    Convert all the pom to pants BUILD underneath certain folder (recursively).
    It iterate through the folder from parent to children, and load properties for children to use.
    """

    namespaces = {"xmlns": "http://maven.apache.org/POM/4.0.0"}

    def __init__(self, root):

        # Keep all the properties find
        self.properties = {}
        self.root = root

    def load_properties(self, root):

        ps = root.findall('xmlns:properties', pom_2_pants.namespaces)

        for p in ps:
            for child in p.findall('*'):
                print(self.remove_namespace(child.tag), child.attrib, child.text)


                self.properties[self.remove_namespace(child.tag)] = child.text

        print (self.properties)

    def remove_namespace(self, tag):

        if tag.find('{http://maven.apache.org/POM/4.0.0}') == 0:
            tag = tag[len('{http://maven.apache.org/POM/4.0.0}'):]
        return tag

    def convert_onefile(self, pomfile):
        print ("Converting ", pomfile)

        pom = xml.parse(pomfile)
        root = pom.getroot()
        self.print_pom_oject(root)
        self.load_properties(root)

        buildfile = self.get_build_file_path(pomfile)
        # if os.path.isfile(buildfile):
        #     print("{0} already exised, stop here".format(buildfile))
        #     exit(1)
        #
        bf = open(buildfile, "w")

        content = self.get_build_content(root)
        print(content, file=bf)

        print("Done with ", pomfile)

    def get_build_content(self, pomroot):


        content = ""




        return content



    def get_build_file_path(self, pomFilepath):
        return pomFilepath[:len(pomFilepath) - len(pom_file_name)] + build_file_name

    def print_pom_oject(self, root):

        print ("{0} - {1} - {2}".format(self.remove_namespace(root.tag), root.attrib, root.text))

        for c in root:
            self.print_pom_oject(c)


    def convert_directory(self):
        poms = self.find_all_poms()

        for pom in poms:
            self.convert_onefile(pom)


    def find_all_poms(self):
        """
        Find all poms under root,
        the order of return decide the order of converting, so need be pre-order
        :return:
        """

        poms = []

        for path, dirs, files in os.walk(self.root):
            if "pom.xml" in files:
                pomfile = os.path.join(path, "pom.xml")
                print (self.get_build_file_path(pomfile))
                poms.append(pomfile)

        return poms

    def mis(self):

        pomFile = xml.parse('/Users/jiezhong.mo/repos/data-science/pom.xml')
        root = pomFile.getroot()

        namespaces = {"xmlns": "http://maven.apache.org/POM/4.0.0"}

        print(root.tag, root.attrib)

        ps = root.findall('xmlns:properties', namespaces)

        for p in ps:
            for child in p.findall('*'):
                print(child.tag, child.attrib, child.text)


def main():
    parser = argparse.ArgumentParser(description='Convert pom to pants build')

    parser.add_argument('-d', '--directory', help='The root path of project,')
    args = parser.parse_args()
    if args.directory:
        root_dir = args.directory.strip()
    else:
        root_dir = "."

    print ('converting folder "{0}" ... \n\n'.format(root_dir))

    p2p = pom_2_pants(root_dir)
    p2p.convert_directory()

    print ('\n\nDone converting "{0}" ... '.format(root_dir))

if __name__ == "__main__":
    main()



#
# for mapping in root.findall('project/Properties'):
#     for prop in mapping.findall('.'):
#         print(prop)
#




