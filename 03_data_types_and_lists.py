project = "VeriRag"
pages= 42
accuracy=0.87
is_public = True
print(type(project), type(pages), type(accuracy), type(is_public))

print(pages * 2)
print(pages / 5)
print(pages // 5)
print(accuracy *100, "%")

print(project.upper())
print(project.lower())
print(len(project))

pages_text = "120"
print(int(pages_text) + 10)

docs = ["policy.pdf", "manual.pdf", "lease.pdf"]

print(docs)
print(len(docs))
print(docs[0])
print(docs[-1])
print(docs[0:2])

docs.append("insurance.pdf")
print(docs)

print("lease.pdf" in docs)


