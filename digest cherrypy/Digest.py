import re


class Digest():
    enzymelist = []
    selectedenzyme = []
    def __init__(self, elist):
        self.enzymelist = elist

    def selectenzyme(self, chosen = [] , allselect = False):
        if allselect:
            self.selectedenzyme = self.enzymelist
        else:
            for i in chosen:
                self.selectedenzyme.append(self.enzymelist[i])

    def digest(self,seq):
        result = []
        seq = self.seq_formation(seq)
        for enzyme in self.selectedenzyme:
            pos = []
            if enzyme[1] == 1:
                pattern = re.compile(enzyme[2])
                m = pattern.search(seq)            
                while(m):
                    start = m.start()
                    pos.append(str(start+int(enzyme[3])))
                    m = pattern.search(seq,m.start()+1)
            else:
                re_l = enzyme[2].split(',')
                pos_l_t = enzyme[3].split(',')
                pos_l = []
                for i in pos_l_t:
                    pos_l.append( int(i))
                for i in range(len(re_l)):
                    pattern = re.compile(re_l[i])
                    m = pattern.search(seq)
                    while(m):
                        start = m.start()
                        pos.append(str(start+pos_l[i]))
                        m = pattern.search(seq,m.start()+1)
                pos = list(set(pos)).sort()

            result.append(pos)

        return result
    
    def seq_formation(self,seq):
        seq = seq.upper()
        l = seq.split('\n')
        if seq[0] == '>':
            seq = ''.join(l[1:])
        else:
            seq = ''.join(l)
        return ''.join(seq.split())

    def is_legal(self,seq):
        pattern = re.compile('[^ACDEFGHIKLMNPQRSTVWY]')
        match = pattern.match(seq)
        if match:
            return False
        else:
            return True
    def output_seq(self,seq):
        result_seq = []
        result_num = []
        output_seq = []
        output_num = []
        for i in range(0,len(seq)-10,10):
            seq_temp = ' '
            seq_temp += seq[i:i+10]
            result_seq.append(seq_temp)
            result_num.append(i+10)
        if len(seq) % 10 != 0:
            seq_temp = ' '
            seq_temp += seq[len(seq)/10 *10:len(seq)]
            result_seq.append(seq_temp)
            result_num.append(len(seq))
        
        for i in range(0,len(result_seq)-6,6):
            temp = []
            for j in range(i,i+6):
                temp.append(result_num[j])
            output_num.append(temp)
            temp = []
            for j in range(i,i+6):
                temp.append(result_seq[j])
            output_seq.append(temp)
            
        temp = []
        for j in range((len(result_seq)-1)/6 *6,len(result_seq)):
            temp.append(result_num[j])
        output_num.append(temp)
        temp = []
        for j in range((len(result_seq)-1)/6 *6,len(result_seq)):
            temp.append(result_seq[j])
        output_seq.append(temp)
        output = []
        for i in range(len(output_num)):
            output.append(output_num[i])
            output.append(output_seq[i])
        return output

test = False
if test:
    import model
    el = model.enzymes()
    chosen = []
    #s = 'qweaaaadssss22aaaadssss333aaaadssss44waaaadssssr'
    s = raw_input()
    o = Digest(el.enzyme)
    o.selectenzyme(allselect=True)
    a = o.digest(s.upper())
