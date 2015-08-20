from .baseservice import BaseService

from .components import Multipart_File, Mylibrary_File, Mylibrary_Folder, Result_Set

# MyLibrary Endpoints
class MyLibraryService(BaseService):

    # Files endpoints
    def get_files(self, limit = 50, sort_by = 'CREATED_DATE_DESC', source = 'ALL', file_type = 'ALL'):
        queries = {}
        queries['limit'] = limit
        queries['sort_by'] = sort_by
        queries['source'] = source
        queries['type'] = file_type

        response = self.request('get', 'library/files', params = queries)
        try:
            response['results']
        except:
            return response
        for i in range(len(response['results'])):
            response['results'][i] = Mylibrary_File(response['results'][i])
        return Result_Set(response)

    # Accepts a Multipart_File or a dict
    def post_files(self, multipart_file):
        attributes = [
            'data',
            'description',
            'file_name',
            'file_type',
            'folder_id',
            'source'
        ]
        form_file, form_data = self.prepare_multipart_body(multipart_file, attributes)

        return self.request('post', 'library/files', form_file = form_file, form_data = form_data)

    # Accepts a list of file_ids or Mylibrary_Files
    # There is no component for file upload status, so a list of dicts will be returned.
    def get_files_upload_status(self, file_ids):
        ids = ''
        for file_id in file_ids:
            if type(file_id) is Mylibrary_File:
                ids = ids + file_id.get_id() + ','
            elif type(file_id) is str:
                ids = ids + file_id + ','
            else:
                raise TypeError('Unknown type for file_id: '+type(file_id).__name__)

        # strip out the last comma
        ids = ids[:-1]

        return self.request('get', 'library/files/uploadstatus/' + ids)

    def get_file(self, file_id):
        file_id = self.file_to_id(file_id)
        return Mylibrary_File(self.request('get', 'library/files/' + file_id))

    def update_file(self, mylibrary_file, include_payload = True):
        params = {'include_payload' : include_payload}
        mylibrary_file = self.validate_file(mylibrary_file)

        return Mylibrary_File(self.request('put', 'library/files/' + mylibrary_file.get_id(), body = mylibrary_file, params = params))

    def delete_file(self, file_id):
        file_id = self.file_to_id(file_id)
        return self.request('delete', 'library/files/' + file_id)

    # Folders endpoints
    def get_folders(self, limit = 50, sort_by = 'CREATED_DATE_DESC'):
        queries = {}
        queries['limit'] = limit
        queries['sort_by'] = sort_by

        response = self.request('get', 'library/folders', params = queries)
        try:
            response['results']
        except:
            return response
        for i in range(len(response['results'])):
            response['results'][i] = Mylibrary_Folder(response['results'][i])
        return Result_Set(response)

    def post_folders(self, folder):
        folder = self.validate_folder(folder)
        return Mylibrary_Folder(self.request('post', 'library/folders', body = folder))

    def get_folder(self, folder_id):
        folder_id = self.folder_to_id(folder_id)
        return Mylibrary_Folder(self.request('get', 'library/folders/' + folder_id))

    def update_folder(self, folder):
        folder = self.validate_folder(folder)
        return Mylibrary_Folder(self.request('put', 'library/folders/' + folder.get_id(), body = folder))

    def delete_folder(self, folder_id):
        folder_id = self.folder_to_id(folder_id)
        return self.request('delete', 'library/folders/' + folder_id)

    def get_folder_files(self, folder_id, limit = 50):
        queries = {}
        queries['limit'] = limit

        folder_id = self.folder_to_id(folder_id)
        return self.request('get', 'library/folders/' + folder_id + '/files', params = queries)
        try:
            response['results']
        except:
            return response
        for i in range(len(response['results'])):
            response['results'][i] = Mylibrary_Folder(response['results'][i])
        return Result_Set(response)

    # Accepts a list of file_ids or Mylibrary_Files
    def move_folder_files(self, folder_id, file_ids):
        folder_id = self.folder_to_id(folder_id)
        ids = []
        for file_id in file_ids:
            if type(file_id) is Mylibrary_File:
                ids.append(file_id.get_id())
            elif type(file_id) is str:
                ids.append(file_id)
            else:
                raise TypeError('Unknown type for file_id: '+type(file_id).__name__)

        return self.request('put', 'library/folders/' + folder_id + '/files', body = ids)

    # Trash endpoints
    def get_trash(self, limit = 50, sort_by = 'CREATED_DATE_DESC', file_type = 'ALL'):
        queries = {}
        queries['limit'] = limit
        queries['sort_by'] = sort_by
        queries['type'] = file_type

        response = self.request('get', 'library/folders/trash/files', params = queries)
        try:
            response['results']
        except:
            return response
        for i in range(len(response['results'])):
            response['results'][i] = Mylibrary_File(response['results'][i])
        return Result_Set(response)
    def delete_trash(self):
        return self.request('delete', 'library/folders/trash/files')

    # Mylibrary info endpoint
    # Returns a dict as there is for component for mylibrary info
    def get_mylibrary_info(self):
        return self.request('get', 'library/info')

    def validate_file(self, mylibrary_file):
        if type(mylibrary_file) is dict:
            mylibrary_file = Mylibrary_File(mylibrary_file)
        if type(mylibrary_file) is not Mylibrary_File:
            raise TypeError('invalid type for Mylibrary file: '+type(mylibrary_file).__name__)

        return mylibrary_file

    def validate_folder(self, folder):
        if type(folder) is dict:
            folder = Mylibrary_Folder(folder)
        if type(folder) is not Mylibrary_Folder:
            raise TypeError('invalid type for Mylibrary folder: '+type(folder).__name__)

        return folder

    def file_to_id(self, file_id):
        if type(file_id) is Mylibrary_File:
            file_id = file_id.get_id()
        return file_id

    def folder_to_id(self, folder_id):
        if type(folder_id) is Mylibrary_Folder:
            folder_id = folder_id.get_id()
        return folder_id






