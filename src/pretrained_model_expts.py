# from keras import backend as K
from data_provision_att_vqa import *
if __name__ == '__main__':
	data_provision_att_vqa = DataProvisionAttVqa("../data_vqa", "")
	# input = K.placeholder(shape=(None, 196, 512))
	print data_provision_att_vqa