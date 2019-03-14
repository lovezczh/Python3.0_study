import click

@click.command()
@click.argument('infa1')
@click.argument('infa2')
@click.argument('out')



def main(infa1,infa2,out):
    fasta = [ ]
    blast = [ ]
    result = [ ]
    
    with open(infa1,'r') as f1:
        with open(infa2,'r') as f2:
            with open(out,'w') as f3:
                for i in f1:
                    if i.startswith("#"):
                        pass
                    else:
                        i = i.strip().split()[0]
                        blast.append(i)
                
                for i in f2.readlines():
                    i = i.strip()
                    if i.startswith(">"):
                        i = i.strip().split(">")[1]
                        fasta.append(i)
                    else:
                        pass
                
                result = "\n".join(set(fasta) - set(blast))
                f3.write(result)
                
if __name__ == '__main__':
    main()
