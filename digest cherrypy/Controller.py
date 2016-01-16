import cherrypy
import operator, os, pickle, sys
from genshi.template import TemplateLoader
from formencode import Invalid
from genshi.filters import HTMLFormFiller
from Digest import Digest

import model
current_dir = os.path.dirname(os.path.abspath(__file__))


enzymelist = model.enzymes()

loader = TemplateLoader(
    os.path.join(os.path.dirname(__file__), 'web'),
    auto_reload=True
)


#enzyme_name = ['Arg-C proteinase', 'Asp-N endopeptidase', 'BNPS-Skatole', 'Caspase1', 'Caspase2', 'Caspase3', 'Caspase4', 'Caspase5', 'Caspase6', 'Caspase7', 'Caspase8', 'Caspase9', 'Caspase10', 'Clostripain(Clostridiopeptidase B', 'CNBr', 'Enterokinase', 'Factor Xa', 'Formic acid', 'Glutamyl endopeptidase', 'GranzymeB', 'Hydroxylamine', 'Iodosobenzoic acid', 'LysC', 'Neutrophil elastase', 'NTCB(2-nitro-5-thiocyanobenzoic acid)', 'Pepsin(pH>2)', 'Proline-endopeptidase', 'Proteinase K', 'Staphylococcal peptidase I', 'Thermolysin']
enzyme_name = []
for i in enzymelist.enzyme:
    enzyme_name.append(i[0])
    
enzyme_id = list(range(len(enzyme_name)))
enzyme_list = zip(enzyme_name,enzyme_id)
#print enzymelist.enzyme
digest = Digest(enzymelist.enzyme)


class ProteinDigest:

    seqmass = 0
    output = ''
    seq1 = ''
    digest_result = ''
    
    @cherrypy.expose
    def index(self, cancel=False, **data):
        if cherrypy.request.method == 'POST':


            seq = data['sequence'].encode()
            self.seq1 = seq
            chosen = []
            try:
                checklist = data['check']
            except KeyError:
                raise cherrypy.HTTPRedirect('/empty')
            if type(checklist) is unicode:
                chosen.append(int(checklist.encode()))
            else:
                for check in checklist:
                    chosen.append(int(check.encode()))
            print chosen
            digest.selectenzyme(chosen)
            self.digest_result = digest.digest(seq)
            chosen_name = []
            result_formatted = []
            result_count = []
            for i in chosen:
                chosen_name.append(digest.enzymelist[i][0])
            for i in self.digest_result:
                if not i:
                    k = 'None.'
                    result_count.append(0)
                else:
                    result_count.append(len(i))
                    k = ' '.join(i)
                result_formatted.append(k)
            self.output = zip(chosen_name,result_formatted,result_count)
            try:

                raise cherrypy.HTTPRedirect('/result')
            except Invalid, e:
                errors = e.unpack_errors()
        else:
            errors={}
        tmpl = loader.load('digest.html')
        stream = tmpl.generate(enzymelist = enzyme_list)
        return stream.render('html', doctype='html')

    @cherrypy.expose
    def result(self, cancel=False, **data):
        tmpr = loader.load('result.html')
        #stream = tmpr.generate(out='output')
        self.seq1 = digest.seq_formation(self.seq1)
        seq_len = len(self.seq1)
        sequence = digest.output_seq(self.seq1)
        if not digest.is_legal(self.seq1):
            sequence = "Please input a protein sequence in text or FASTA formation."
            self.output = []
            seq_len = " N/A "
        stream = tmpr.generate(aaa=self.output,sequence=sequence,length=seq_len)
        return stream.render('html', doctype='html')
    
    @cherrypy.expose
    def empty(self, cancel = False):
        return """<h1>Please select at least one enzyme.</h1>
                <a href="/">Back</a>"""



if __name__ == '__main__':

    conf = {'/':{'tools.sessions.on': True,
                 'tools.staticdir.root': current_dir
                 },
            '/static':{'tools.staticdir.on': True,
                        'tools.staticdir.dir': './web/src'
                       },
            
            }
    cherrypy.config.update({'server.socket_port': 8001})

    cherrypy.quickstart(ProteinDigest(),'', config = conf)

