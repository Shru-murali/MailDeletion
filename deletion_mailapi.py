from common import aunthenticate_mail, search_specificmessages

def delete_messages(service, query):
    messages_to_delete = search_specifiedmessages(service, query)
    return service.users().messages().delete(userId = 'exm',id = msg['id'])
      userId='me',
      body={
          'ids': [ msg['id'] for msg in messages_to_delete]
      }
    .execute()

if __name__ == "__main__":
    service = aunthenticate_mail()
    delete_messages(service, "Google")