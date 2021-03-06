import os
import glob

try:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
except:
    ROOT_DIR = "c:/Users/Heitor/Desktop/emacs-24.3/bin/anotacoes/"
    
PAGINAS_DIR = ROOT_DIR + '/paginas/'
HTML_DIR = ROOT_DIR + '/html/'
TUTORIAIS_DIR = ROOT_DIR + '/tutoriais/'

INDEX_FILE = HTML_DIR + "index.html"

if not os.path.exists(os.path.dirname(HTML_DIR + 'tutoriais/')):
    try:
        os.makedirs(os.path.dirname(HTML_DIR + 'tutoriais/'))
    except OSError as e:
        if e.errno != e.EEXIST:
            raise        

HEADER = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Anotações</title>
        <link rel="stylesheet" href="/css/atom-one-light.css">
        <link rel="stylesheet" href="/css/style.css">
    </head>
    <body>"""

def renameExt(filename, extension):        
    files = filename.strip().split('/')
    parts = files[-1].split('.')
    return parts[0] + "." + extension

def md2html(f):
    return f.replace(".md", ".html")

def convert(pagina, anterior=None, proximo=None):
    print("convert", pagina, anterior, proximo)
    if anterior:
        anterior_link = '<a href="/{}">'.format(anterior) + '&lt; Anterior</a>'
    else:
        anterior_link = "&lt; Anterior"

    if proximo:
        proximo_link = '<a href="/{}">'.format(proximo) + 'Próximo &gt;</a>'
    else:
        proximo_link = ""
        
    top = HEADER + '''
        <p>
            <a href="/">Home</a>
        </p>
        <textarea id="raw" style="display: none;">'''

    bottom = '''</textarea>''' + anterior_link + " | " + proximo_link + ''' 

        <div id="formatted"></div>

    ''' + proximo_link + '''
        <script src="/js/jquery.min.js"></script>
        <script src="/js/markdown-it.js"></script>
        <script src="/js/highlight.min.js"></script>
        <script>
         var md = window.markdownit();
         hljs.initHighlightingOnLoad();

         document.getElementById("formatted").innerHTML = md.render(document.getElementById("raw").value);
         $('pre code').each(function(i, block) {
             hljs.highlightBlock(block);
         });
        </script>
    </body>
</html>
'''
    
    md_file = open(PAGINAS_DIR + pagina, encoding="utf-8")
    raw_md = md_file.read()
    md_file.close()

    if not os.path.exists(os.path.dirname(HTML_DIR + pagina)):
        try:
            os.makedirs(os.path.dirname(HTML_DIR + pagina))
        except OSError as e:
            if e.errno != e.EEXIST:
                raise
                
    html_file = open(HTML_DIR + pagina.replace('md', 'html'), 'w', encoding="utf-8")
    print(top + raw_md + bottom, file=html_file)
    html_file.close()

def getLabel(filename):
    f = open(filename, encoding="utf-8")
    label = f.readline()
    label = label.replace("#", "").strip()
    return label

# Begin main script

with open(INDEX_FILE, 'w', encoding="utf-8") as index:
    print(HEADER, file=index)

    for tutorial in sorted(glob.glob(TUTORIAIS_DIR + "/*")):
        tutorial = tutorial.replace('\\', '/')
        tutorial_html_name = renameExt(tutorial, 'html')

        with open(tutorial, encoding="utf-8") as tut, open(HTML_DIR + "tutoriais/" + tutorial_html_name, 'w', encoding="utf-8") as tut_html_contents:
            print(HEADER, file=tut_html_contents)
            print('<p><a href="/">Home</a></p>', file=tut_html_contents)

            tut_label = getLabel(tutorial)
            print('<p><a href="tutoriais/{}">'.format(tutorial_html_name) + tut_label + '</a></p>', file=index)

            items = []
            next(tut)
            for line in tut:
                line = line.strip()
                md_file = line
                label = getLabel(PAGINAS_DIR + md_file)
                items.append((md_file, label))

            for i, item in enumerate(items):
                print('<p><a href="/{}">'.format(md2html(item[0])) + item[1] + "</a></p>", file=tut_html_contents)
                
                if i == 0:
                    anterior = None
                else:
                    anterior = md2html(items[i-1][0])

                if i == len(items) - 1:
                    proximo = None
                else:
                    proximo = md2html(items[i+1][0])
                    
                convert(items[i][0], anterior, proximo)


# end of scripts
print("cd html and Run python -m http.server 8000 , or, php -S 127.0.0.1:8000")
