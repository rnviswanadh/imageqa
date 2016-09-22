# from keras import backend as K
from data_provision_att_vqa import *
if __name__ == '__main__':
	print "Started Loading data"
	data_provision_att_vqa = DataProvisionAttVqa("../data_vqa", "trainval_feat.h5")
	print "Loaded Data"
	# input = K.placeholder(shape=(None, 196, 512))
	print data_provision_att_vqa