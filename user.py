import data
import inputs, utility
import hash

def register(data):
	flag = True
	while flag:
		reg_name = inputs.input_valid('Masukan nama: ', validation = lambda x : filter_name(x), provision = 'Nama hanya terdiri dari alphabet.', flagstop = '!x').title()
		reg_name = utility.remove_space(reg_name)
		if reg_name == '!X': # Karena di title !x -> !X
			return

		reg_username = inputs.input_valid('Masukan username: ', validation = lambda x : filter_username(x), provision = 'Username hanya terdiri dari A-Z, a-z, `_`, `-`, dan 0-9.')
		reg_password = inputs.input_valid('Masukan password (min. 10 karakter): ', validation = lambda x : utility.length(x) >= 10, provision = 'Password minimal 10 karakter.')

		inp = inputs.input_yesorno('Apakah kamu yakin dengan data kamu? ')
		if not inp:
			print('Gagal mendaftarkan user.')
		else:
			flag = False

	if inputs.find_idx_key_with_target(data[0], 1, reg_username) == -1: # User tidak ditemukan
		data[0] += [
			['id', str(utility.length(data[0]) + 1)], 
			['username', reg_username], 
			['nama', reg_name], 
			['password', hash.encrypt(reg_password)],
			['role', 'user'],
			['saldo', '0']
		]
		print(f'Username {reg_username} telah berhasil register ke dalam "Binomo".')
	else:
		print(f'Username {reg_username} sudah terpakai, silakan menggunakan username lain.')

def filter_name(name):
	for i in name:
		if not ((ord('A') <= ord(i) <= ord('Z')) or (ord('a') <= ord(i) <= ord('z')) or (ord(i)) == 32):
			return False
	return True

def filter_username(username):
	for i in username:
		if not ((ord('A') <= ord(i) <= ord('Z')) or (ord('a') <= ord(i) <= ord('z')) or (i == '_') or (i == '-') or (ord('0') <= ord(i) <= ord('9'))):
			return False
	return True

def login(data):
	while True:
		username = inputs.input_valid('Masukan username: ', flagstop = '!x')
		if username == '!x':
			return None
		password = inputs.input_valid('Masukan password: ')
		data_user = data[0] # user.csv
		user_id = inputs.find_idx_key_with_target(data_user, 1, username)
		if user_id != -1 and hash.encrypt(password) == data_user[int(user_id) - 1][3][1]: # password
			print(f'Halo {data_user[int(user_id) - 1][2][1]}! Selamat datang di "Binomo".')
			return data_user[int(user_id) - 1] # id
		else:
			print('Password atau username salah atau tidak ditemukan.')