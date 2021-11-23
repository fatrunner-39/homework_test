documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def show_document_info(document):
    doc_type = document['type']
    doc_number = document['number']
    doc_owner_name = document['name']
    return '{} "{}" "{}"'.format(doc_type, doc_number, doc_owner_name)



def add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name):
    new_doc = {
        "type": new_doc_type,
        "number": new_doc_number,
        "name": new_doc_owner_name
    }
    documents.append(new_doc)
    # append_doc_to_shelf(new_doc_number, new_doc_shelf_number)
    return documents

def check_document_existance(user_doc_number):
    doc_founded = False
    for current_document in documents:
        doc_number = current_document['number']
        if doc_number == user_doc_number:
            doc_founded = True
            break
    return doc_founded

def delete_doc():
    user_doc_number = '11-2' #input('Введите номер документа - ')
    doc_exist = check_document_existance(user_doc_number)
    if doc_exist:
        for current_document in documents:
            doc_number = current_document['number']
            if doc_number == user_doc_number:
                documents.remove(current_document)
                # remove_doc_from_shelf(doc_number)
                return documents, True

if __name__ == '__main__':
    # print(show_document_info(documents[2]))
    print(add_new_doc('passport', '335 111', 'Tisha Scotisha'))
    print(len(documents))
