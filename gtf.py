#新id

import re,io
import csv
import time

def new_id(name): #获得新id与名称的键值对([old_id]:[new_id,new_name]),用空间换时间
    f = csv.reader(open(name,'r'))
    dict_1 = {}
    
    for m in f:
        old=m[0].rfind('.')
        new= m[1].rfind('.')
        dict_1.setdefault(m[0][:old],[]).append(m[1][:new])
        desc = m[2].rfind('[')
        dict_1.setdefault(m[0][:old],[]).append(m[2][:desc-1])
        dict_1.setdefault(m[0][:old],[]).append(m[3])
    return dict_1



if __name__ == '__main__' :
    
    file = io.open('e:\\Milk_FIN.gff3','r')
    gene =  open('d:\\gene.gtf', 'w')
    exon =  open('d:\\exon.gtf', 'w')
    cds = open('d:\\cds.gtf', 'w')
    others=open('d:\\others.gtf',"w")
    dict_1 = new_id("e:\\ID_and_geneName_ww_final.csv") 
    e={}
    for line in file:
        if("#" in line):
            continue;
        line=line.split("\t")#按\t分割
        
        if(line[2] == "mRNA"):
            line[2] = "transcript"
    
        
        temp = line[8].split(";")#第8列按;分割
        attributes = temp[0].split("=") #按=分割
        if(line[2]!="gene"):##如果是一条cds或者是exon
            s = attributes[1].find('.')#Milk01G0001.1.cds6,找到最后一个.
            gene_id = attributes[1][:s] #id是从头到最后一个.之前
        else:
            gene_id = attributes[1]##不是的话，那就直接是gene_id
        if (gene_id in dict_1.keys()):#如果该gen_id有新的id
            gene_name = dict_1[gene_id][2]#得到gene_name
            gene_biotype=dict_1[gene_id][1]
            gene_id = dict_1[gene_id][0]#得到new_id
            if("cds" in temp[0]):
                for i in range(0,8):#前7列内容不变
                    cds.write(line[i]+'\t')
                
                cds.write(gene_id+'\t')
                cds.write(gene_name+'\t')
                cds.write(gene_biotype+'\t')
                cds.write("\n");
            
            elif("gene" in line[2] or "transcript" in line[2]):
                for i in range(0,8):#前7列内容不变
                    gene.write(line[i]+'\t')
                gene.write(gene_id+'\t')
                gene.write(gene_name+'\t')
                gene.write(gene_biotype+'\t')
                gene.write('\n')
                
            elif("exon" in temp[0]):
                for i in range(0,8):#前7列内容不变
                    exon.write(line[i]+'\t')
                exon.write(gene_id+'\t')
                exon.write(gene_name+'\t')
                exon.write(gene_biotype+'\t')
                if gene_id not in e:#If the kmer does not exist in the dictionary, add it to the dictionary 
                    new = {gene_id:0}
                    e.update(new)
                e[gene_id]+=1#kmer number +1 
                exon.write(str(e[gene_id])+'\t')
                exon.write("\n");
            else:
                for i in range(0,8):#前7列内容不变
                    exon.write(line[i]+'\t')
                exon.write(gene_id+'\t')
                exon.write(gene_name+'\t')
                exon.write(gene_biotype+'\t')
                exon.write("\n");
    exon.close()
    cds.close()
    gene.close()
    others.close()
    
    
    
import re,io
import csv
import time

def new_id(name): #获得新id与名称的键值对([old_id]:[new_id,new_name]),用空间换时间
    f = csv.reader(open(name,'r'))
    dict_1 = {}
    
    for m in f:
        old=m[0].rfind('.')
        new= m[1].rfind('.')
        dict_1.setdefault(m[0][:old],[]).append(m[1][:new])
        desc = m[2].rfind('[')
        dict_1.setdefault(m[0][:old],[]).append(m[2][:desc-1])
        dict_1.setdefault(m[0][:old],[]).append(m[3])
    return dict_1



if __name__ == '__main__' :
    

    gene =  open('d:\\gene.gtf', 'r')
    exon =  open('d:\\exon.gtf', 'r')
    cds = open('d:\\cds.gtf', 'r')
    out=open('d:\\result.gtf', 'w')
    l_g=gene.readlines()
    l_e=exon.readlines()
    l_c=cds.readlines()
    e=0;c=0;i=0
    while(i<len(l_g)):
        out.write(l_g[i])
        out.write(l_g[i+1])
        line=l_g[i].split("\t")#按\t分割
        gene_id=line[8]

        while(e<len(l_e)):
            line=l_e[e].split("\t")#按\t分割
            if(line[8]==gene_id):
                out.write(l_e[e])
                e=e+1
            else:
                break;
        i=i+2
    out.close()
    
    
    
import re,io
import csv
import time



if __name__ == '__main__' :
    

    
    r =  open('d:\\result.gtf', 'r')
    cds = open('d:\\cds.gtf', 'r')
    out=open('d:\\result1.gtf', 'w')
    
    i=0;l_c=cds.readlines()
    for line in r.readlines(): 
        m=line.split('\t')
        if("exon" in m[2]):
            out.write(line)
            temp=line.split('\t')
            ii=l_c[i].split('\t')
            if(ii[3]>=temp[3] and ii[4]<=temp[4] and ii[8]==temp[8]):
                t=l_c[i].split('\t')
                for j in range(0,11):
                    out.write(t[j]+'\t')
                out.write(temp[11]+'\n')
                i=i+1
            else:
                continue
        else:
            out.write(line)
            
    out.close()
    
    
r =  open('d:\\result1.gtf', 'r')
out= open("d:\\new_id.gtf","w")
for line in r.readlines():
    m=line.split('\t')
    if("gene" in m[2]):
        line=line.split("\t");
        for i in range(0,8):
            out.write(line[i]+'\t')
        out.write('gene_id \"'+line[8]+'\"; gene_name \"'+line[9]+'\"; '+'gene_biotype \"'+line[10]+'\";'+'\n') 
    elif("transcript" in m[2]):
        line=line.split("\t");
        for i in range(0,8):
            out.write(line[i]+'\t')
        out.write('gene_id \"'+line[8]+'\"; gene_name \"'+line[9]+'\"; '+'gene_biotype \"'+line[10]+'\"; '+'transcript_id \"'+line[8]+'\"; '+'transcript_biotype \"'+line[10]+'\";'+'\n')
        
    elif("exon" in m[2] ):
        line=line.split("\t");
        for i in range(0,8):
            out.write(line[i]+'\t')
        out.write('gene_id \"'+line[8]+'\"; gene_name \"'+line[9]+'\"; '+'gene_biotype \"'+line[10]+'\"; '+'transcript_id \"'+line[8]+'\"; '+'transcript_biotype \"'+line[10]+'\"; '+'exon_number \"'+line[11]+'\";\n')
    elif("CDS" in m[2]):
        line=line.split("\t");
        for i in range(0,8):
            out.write(line[i]+'\t')
        ttt=line[11].split('\n')
        out.write('gene_id \"'+line[8]+'\"; gene_name \"'+line[9]+'\"; '+'gene_biotype \"'+line[10]+'\"; '+'transcript_id \"'+line[8]+'\"; '+'transcript_biotype \"'+line[10]+'\"; '+'exon_number \"'+ttt[0]+'\";\n')
    
    else:
        line=line.split("\t");
        for i in range(0,8):
            out.write(line[i]+'\t')
        out.write('gene_id \"'+line[8]+'\"; gene_name \"'+line[9]+'\"; '+'gene_biotype \"'+line[10]+'\";'+'\n') 
        
out.close()



'''


#旧id
import re,io
import csv
import time

def new_id(name): #获得新id与名称的键值对([old_id]:[new_id,new_name]),用空间换时间
    f = csv.reader(open(name,'r'))
    dict_1 = {}
    
    for m in f:
        old=m[0].rfind('.')
        new= m[1].rfind('.')
        dict_1.setdefault(m[0][:old],[]).append(m[1][:new])
        desc = m[2].rfind('[')
        dict_1.setdefault(m[0][:old],[]).append(m[2][:desc-1])
        dict_1.setdefault(m[0][:old],[]).append(m[3])
    return dict_1



if __name__ == '__main__' :
    
    file = io.open('e:\\Milk_FIN.gff3','r')
    gene =  open('d:\\gene.gtf', 'w')
    exon =  open('d:\\exon.gtf', 'w')
    cds = open('d:\\cds.gtf', 'w')
    others=open('d:\\others.gtf',"w")
    dict_1 = new_id("e:\\ID_and_geneName_ww_final.csv") 
    e={}
    for line in file:
        if("#" in line):
            continue;
        line=line.split("\t")#按\t分割
        
        if(line[2] == "mRNA"):
            line[2] = "transcript"
    
        
        temp = line[8].split(";")#第8列按;分割
        attributes = temp[0].split("=") #按=分割
        if(line[2]!="gene"):##如果是一条cds或者是exon
            s = attributes[1].find('.')#Milk01G0001.1.cds6,找到最后一个.
            gene_id = attributes[1][:s] #id是从头到最后一个.之前
        else:
            gene_id = attributes[1]##不是的话，那就直接是gene_id
        if (gene_id not in dict_1.keys()):#如果该gen_id有新的i
        
            if("cds" in temp[0]):
                for i in range(0,8):#前7列内容不变
                    cds.write(line[i]+'\t')
                
                cds.write(gene_id+'\t')

                cds.write("\n");
            elif("exon" in temp[0]):
                for i in range(0,8):#前7列内容不变
                    exon.write(line[i]+'\t')
                exon.write(gene_id+'\t')

                if gene_id not in e:
                    new = {gene_id:0}
                    e.update(new)
                e[gene_id]+=1#kmer number +1 
                exon.write(str(e[gene_id])+'\t')
                exon.write("\n");
            elif("gene" in line[2] or "transcript" in line[2]):
                for i in range(0,8):#前7列内容不变
                    gene.write(line[i]+'\t')
                gene.write(gene_id+'\t')
                gene.write('\n')
                
            else:
                for i in range(0,8):#前7列内容不变
                    exon.write(line[i]+'\t')
                exon.write(gene_id+'\t')
                exon.write('\n')
    exon.close()
    cds.close()
    gene.close()
    others.close()
    
    
    


 
import re,io
import csv
import time

def new_id(name): #获得新id与名称的键值对([old_id]:[new_id,new_name]),用空间换时间
    f = csv.reader(open(name,'r'))
    dict_1 = {}
    
    for m in f:
        old=m[0].rfind('.')
        new= m[1].rfind('.')
        dict_1.setdefault(m[0][:old],[]).append(m[1][:new])
        desc = m[2].rfind('[')
        dict_1.setdefault(m[0][:old],[]).append(m[2][:desc-1])
        dict_1.setdefault(m[0][:old],[]).append(m[3])
    return dict_1



if __name__ == '__main__' :
    

    gene =  open('d:\\gene.gtf', 'r')
    exon =  open('d:\\exon.gtf', 'r')
    cds = open('d:\\cds.gtf', 'r')
    out=open('d:\\result.gtf', 'w')
    l_g=gene.readlines()
    l_e=exon.readlines()
    l_c=cds.readlines()
    e=0;c=0;i=0
    while(i<len(l_g)):
        out.write(l_g[i])
        out.write(l_g[i+1])
        line=l_g[i].split("\t")#按\t分割
        gene_id=line[8]
        print(gene_id)
        while(e<len(l_e)):
            line=l_e[e].split("\t")#按\t分割
            if(line[8]==gene_id):
                out.write(l_e[e])
                e=e+1
            else:
                break;
        i=i+2
    out.close()
    
    





import re,io
import csv
import time



if __name__ == '__main__' :
    

    
    r =  open('d:\\result.gtf', 'r')
    cds = open('d:\\cds.gtf', 'r')
    out=open('d:\\result1.gtf', 'w')
    
    i=0;l_c=cds.readlines()
    for line in r.readlines(): 
        m=line.split('\t')
        if("exon" in m[2]):
            out.write(line)
            temp=line.split('\t')
            ii=l_c[i].split('\t')
            if(ii[3]>=temp[3] and ii[4]<=temp[4] and ii[8]==temp[8]):
                t=l_c[i].split('\t')
                for j in range(0,9):
                    out.write(t[j]+'\t')
                out.write(temp[9]+'\n')
                i=i+1
            else:
                continue
        else:
            out.write(line)
            
    out.close()
    
    
    
    
    
r =  open('d:\\result1.gtf', 'r')
out= open("d:\\old_id.gtf","w")
for line in r.readlines():
    m=line.split('\t')
    if("gene" in m[2]):
        line=line.split("\t");
        for i in range(0,8):
            out.write(line[i]+'\t')
        out.write('gene_id \"'+line[8]+'\"; gene_name \"'+line[8]+'\"; '+'\n') 
    elif("transcript" in m[2]):
        line=line.split("\t");
        for i in range(0,8):
            out.write(line[i]+'\t')
        out.write('gene_id \"'+line[8]+'\"; gene_name \"'+line[8]+'\"; '+'transcript_id \"'+line[8]+'\"; '+'\n')
        
    elif("exon" in m[2] ):
        line=line.split("\t");
        for i in range(0,8):
            out.write(line[i]+'\t')
        out.write('gene_id \"'+line[8]+'\"; gene_name \"'+line[8]+'\"; '+'transcript_id \"'+line[8]+'\"; '+'exon_number \"'+line[9]+'\";\n')
    elif("CDS" in m[2]):
        line=line.split("\t");
        for i in range(0,8):
            out.write(line[i]+'\t')
        ttt=line[9].split('\n')
        out.write('gene_id \"'+line[8]+'\"; gene_name \"'+line[8]+'\"; '+'transcript_id \"'+line[8]+'\"; '+'exon_number \"'+ttt[0]+'\";\n')
    
    else:
        line=line.split("\t");
        for i in range(0,8):
            out.write(line[i]+'\t')
        out.write('gene_id \"'+line[8]+'\"; gene_name \"'+line[8]+'\"; '+'\n') 
out.close()
'''