import sys

template = """
<?xml version="1.0" encoding="utf-8" ?>                                            
<config>                                                                           
    <description>%s</description>                                            
    <source_groups>                                                                
                <header_search_paths>                                              
                        %s
                </header_search_paths>                                             
        <source_group_0f076239-dd78-43a2-acd8-b6b3013a0fec>                        
            <build_file_path>                                                      
                    <compilation_db_path>%s</compilation_db_path>
            </build_file_path>                                                     
            <name>C/C++ from Compilation Database</name>                           
            <pch_flags>                                                            
                <use_compiler_flags>1</use_compiler_flags>                         
            </pch_flags>                                                           
            <status>enabled</status>                                               
            <type>C/C++ from Compilation Database</type>                           
        </source_group_0f076239-dd78-43a2-acd8-b6b3013a0fec>                       
    </source_groups>                                                               
    <version>8</version>                                                           
</config>
"""

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("./create_template.py <name> <full_path_to_compile_commands.json> [<optional_path_to_headers>]")
    sys.exit(-1)
  prj_name = sys.argv[1]
  cc_path = sys.argv[2]
  includes = []
  if len(sys.argv) > 2:
    for p in sys.argv[3:]:
      includes.append("<header_search_path>%s</header_search_path>" % p)
  
  print(template % (prj_name, "\n\t\t\t".join(includes), cc_path))
