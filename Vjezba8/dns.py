
import dns.resolver
import dns.reversename

HOST = 'python.org'
for qtype in ['A','AAAA','CNAME','MX','NS']:
    answers = dns.resolver.query(HOST, qtype, raise_on_no_answer = False)
    print('Iteration')
    for answer in answers:
        print(answer)
    print("RRset")
    if answers.rrset is not None:
        print(answers.rrset)

host_reversed = dns.reversename.from_address("213.149.62.241")
print("Reverse lookup " + host_reversed.__str__())
print("Lookup from reversed lookup " + dns.reversename.to_address(host_reversed).decode())