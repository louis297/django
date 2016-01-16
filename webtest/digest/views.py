from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic

from .models import EnzymeList
from .Digest import Digest

def index(request):
    enzyme_list = EnzymeList.objects.using('digestdb').order_by('id')
    
    template = loader.get_template('digest/digest.html')
    context = {
        'enzyme_list': enzyme_list,
    }
    return HttpResponse(template.render(context, request))

def result(request):
    enzyme_selected_id = []
    enzyme_selected_name = []
    for i in request.POST:
        if i.encode().startswith('check'):
            enzyme_selected_id.append(int(request.POST[i])-1)

    #if no enzyme selected, return an error page named 'empty'
    if not enzyme_selected_id:
        return HttpResponseRedirect('/digest/empty')
    enzyme_selected_id.sort()
    
    #parsing format of enzyme_list, for previous written Digest class
    #   since this is only a transplant work
    enzyme_list_db = EnzymeList.objects.using('digestdb').all().order_by('id')
    enzyme_list = []
    for i in enzyme_list_db:
        if i.id in enzyme_selected_id:
            enzyme_selected_name.append(i.name)
        enzyme_list.append([i.name, i.amount, i.digest, i.start_pos])
    seq = request.POST['sequence'].encode()
    digest = Digest(enzyme_list)
    digest.selectenzyme(enzyme_selected_id)
    digest_result = digest.digest(seq)

    #output data format
    result_formatted = []
    result_count = []
    for i in digest_result:
        if not i:
            temp = 'None.'
            result_count.append(0)
        else:
            result_count.append(len(i))
            temp = ' '.join(i)
        result_formatted.append(temp)
    output = zip(enzyme_selected_name,result_formatted,result_count)

    seq1 = request.POST['sequence'].encode()
    seq1 = digest.seq_formation(seq1)
    seq_len = len(seq1)
    sequence = digest.output_seq(seq1)
    if not digest.is_legal(seq1):
        sequence = "Please input a protein sequence in text or FASTA formation."
        self.output = []
        seq_len = " N/A "
    print sequence
    #load template and output the page
    template = loader.get_template('digest/result.html')
    context = {
        'digest_result' : output,
        'sequence' : sequence,
        'seq_length' : seq_len
    }
    return HttpResponse(template.render(context, request))

def empty(self, cancel = False):
    return HttpResponse("""<h1>Please select at least one enzyme.</h1>
            <a href="/digest">Back</a>""")
