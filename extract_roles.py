import os
from docx import Document

def extract_roles_from_docx(docx_path):
    doc = Document(docx_path)
    roles = set()
    for para in doc.paragraphs:
        text = para.text.strip()
        if any(word in text.lower() for word in ["rol", "actor", "perfil", "usuario"]):
            roles.add(text)
    return roles

def main():
    folder = "e:/repositorios/redSismica/documentos"
    all_roles = set()
    for filename in os.listdir(folder):
        if filename.endswith(".docx"):
            path = os.path.join(folder, filename)
            roles = extract_roles_from_docx(path)
            all_roles.update(roles)
    print("Roles encontrados:")
    for role in all_roles:
        print(role)

if __name__ == "__main__":
    main()
