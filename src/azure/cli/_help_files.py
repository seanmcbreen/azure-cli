import yaml

def _load_help_file(delimiters):
    helps = {'test_group1.test_group2': """
                type: group
                short-summary: this module does xyz one-line or so
                long-summary: |
                    this module.... kjsdflkj... klsfkj paragraph1
                    this module.... kjsdflkj... klsfkj paragraph2
                examples:
                    - name: foo example
                      text: example details
             """,
             'login': """
                type: command
                short-summary: this module does xyz one-line or so
                long-summary: |
                    this module.... kjsdflkj... klsfkj paragraph1
                    this module.... kjsdflkj... klsfkj paragraph2
                parameters: 
                    - name: --username/-u
                      type: string
                      required: False
                      short-summary: one line partial sentence
                      long-summary: text, markdown, etc.
                      populator-commands: 
                          - az vm list
                          - default
                    - name: --service-principal
                      type: string
                      short-summary: one line partial sentence, except that this one is a little bit longer than one line, how do we handle line wrapping?
                      long-summary: |
                        paragraph(s)
                        paragraph(s)
                        This is a long paragraph with text that wraps down to the next line.  The text is broken up by the wrap method after 100 chars.
                    - name: --tenant/-t
                      type: string
                      short-summary: one line partial sentence
                      long-summary: paragraph(s)
                examples:
                    - name: foo example
                      text: example details
             """,
             'account': """
                 type: group
                 short-summary: this module does xyz one-line or so
                 long-summary: |
                     this module.... kjsdflkj... klsfkj paragraph1
                     this module.... kjsdflkj... klsfkj paragraph2
                 parameters: 
                     - name: --username/-u
                       type: string
                       required: false
                       short-summary: one line partial sentence
                       long-summary: text, markdown, etc.
                       populator-commands:
                           - az vm list
                           - default
                     - name: --password/-p
                       type: string
                       short-summary: one line partial sentence
                       long-summary: paragraph(s)
                     - name: --service-principal
                       type: string
                       short-summary: one line partial sentence
                       long-summary: paragraph(s)
                     - name: --tenant/-t
                       type: string
                       short-summary: one line partial sentence
                       long-summary: paragraph(s)
                 examples:
                     - name: foo example
                       text: example details
                """,
             'azure-cli': 'detailed intro help'
            }

    if delimiters in helps:
        return yaml.load(helps[delimiters])
    else:
        return None