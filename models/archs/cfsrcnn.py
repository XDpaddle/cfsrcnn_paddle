import paddle
import paddle.nn as nn
import models.archs.ops as ops
        

class Net(nn.Layer):
    def __init__(self, scale, **kwargs):
        super(Net, self).__init__()
        
        self.scale = scale #value of scale is scale. 
        multi_scale = 0 # value of multi_scale is multi_scale in args.
        group = 1 #if valule of group isn't given, group is 1.
        kernel_size = 3 #tcw 201904091123
        kernel_size1 = 1 #tcw 201904091123
        padding1 = 0 #tcw 201904091124
        padding = 1     #tcw201904091123
        features = 64   #tcw201904091124
        groups = 1       #tcw201904091124
        channels = 3
        features1 = 64
        self.sub_mean = ops.MeanShift((0.4488, 0.4371, 0.4040), sub=True)
        self.add_mean = ops.MeanShift((0.4488, 0.4371, 0.4040), sub=False)
        '''
           in_channels, out_channels, kernel_size, stride, padding,dialation, groups,
        '''
        self.conv1 = nn.Sequential(nn.Conv2D(in_channels=channels,out_channels=features,kernel_size=kernel_size,padding=padding,groups=1,bias_attr=False))
        self.conv2 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size1,padding=0,groups=1,bias_attr=False), nn.ReLU())
        self.conv3 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=padding,groups=groups,bias_attr=False))
        self.conv4 = nn.Sequential(nn.Conv2D(in_channels=2*features,out_channels=features,kernel_size=kernel_size1,padding=0,groups=1,bias_attr=False), nn.ReLU())
        self.conv5 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=padding,groups=groups,bias_attr=False))
        self.conv6 = nn.Sequential(nn.Conv2D(in_channels=2*features,out_channels=features,kernel_size=kernel_size1,padding=0,groups=1,bias_attr=False), nn.ReLU())
        self.conv7 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=padding,groups=groups,bias_attr=False))
        self.conv8 = nn.Sequential(nn.Conv2D(in_channels=2*features,out_channels=features,kernel_size=kernel_size1,padding=0,groups=1,bias_attr=False),nn.ReLU())
        self.conv9 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=padding,groups=groups,bias_attr=False))
        self.conv10 = nn.Sequential(nn.Conv2D(in_channels=2*features,out_channels=features,kernel_size=kernel_size1,padding=0,groups=1,bias_attr=False),nn.ReLU())
        self.conv11 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=padding,groups=groups,bias_attr=False))
        self.conv12 = nn.Sequential(nn.Conv2D(in_channels=2*features,out_channels=features,kernel_size=kernel_size1,padding=0,groups=1,bias_attr=False),nn.ReLU())
        self.conv13 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=padding,groups=groups,bias_attr=False))
        self.conv14 = nn.Sequential(nn.Conv2D(in_channels=2*features,out_channels=features,kernel_size=kernel_size1,padding=0,groups=1,bias_attr=False),nn.ReLU())
        self.conv15 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=padding,groups=groups,bias_attr=False))
        self.conv16 = nn.Sequential(nn.Conv2D(in_channels=2*features,out_channels=features,kernel_size=kernel_size1,padding=0,groups=1,bias_attr=False),nn.ReLU())
        self.conv17 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=padding,groups=groups,bias_attr=False))
        self.conv18 = nn.Sequential(nn.Conv2D(in_channels=2*features,out_channels=features,kernel_size=kernel_size1,padding=0,groups=1,bias_attr=False),nn.ReLU())
        self.conv19 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=padding,groups=groups,bias_attr=False))
        self.conv20 = nn.Sequential(nn.Conv2D(in_channels=2*features,out_channels=features,kernel_size=kernel_size1,padding=0,groups=1,bias_attr=False), nn.ReLU())
        self.conv21 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=padding,groups=groups,bias_attr=False))
        self.conv22 = nn.Sequential(nn.Conv2D(in_channels=2*features,out_channels=features,kernel_size=kernel_size1,padding=0,groups=1,bias_attr=False), nn.ReLU())
        self.conv23 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=padding,groups=groups,bias_attr=False))
        self.conv24 = nn.Sequential(nn.Conv2D(in_channels=2*features,out_channels=features,kernel_size=kernel_size1,padding=0,groups=1,bias_attr=False),nn.ReLU())
        self.conv25 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=padding,groups=groups,bias_attr=False))
        self.conv26 = nn.Sequential(nn.Conv2D(in_channels=2*features,out_channels=features,kernel_size=kernel_size1,padding=0,groups=1,bias_attr=False),nn.ReLU())
        self.conv27 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=padding,groups=groups,bias_attr=False))
        self.conv28 = nn.Sequential(nn.Conv2D(in_channels=2*features,out_channels=features,kernel_size=kernel_size1,padding=0,groups=1,bias_attr=False),nn.ReLU())
        self.conv29 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=padding,groups=groups,bias_attr=False))
        self.conv30 = nn.Sequential(nn.Conv2D(in_channels=2*features,out_channels=features,kernel_size=kernel_size1,padding=0,groups=1,bias_attr=False),nn.ReLU())
        self.conv31 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=padding,groups=groups,bias_attr=False))
        self.conv32 = nn.Sequential(nn.Conv2D(in_channels=2*features,out_channels=features,kernel_size=kernel_size1,padding=0,groups=1,bias_attr=False),nn.ReLU())
        self.conv33 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=padding,groups=groups,bias_attr=False))
        self.conv34 = nn.Sequential(nn.Conv2D(in_channels=2*features,out_channels=features,kernel_size=kernel_size,padding=1,groups=1,bias_attr=False))
        self.conv35 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=1,groups=1,bias_attr=False),nn.ReLU())
        self.conv36 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=1,groups=1,bias_attr=False),nn.ReLU())
        self.conv37 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=1,groups=1,bias_attr=False),nn.ReLU())
        self.conv38 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=1,groups=1,bias_attr=False),nn.ReLU())
        self.conv39 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=1,groups=1,bias_attr=False),nn.ReLU())
        self.conv34_1 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=1,groups=1,bias_attr=False))
        self.conv34_2 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=1,groups=1,bias_attr=False))    
        self.conv34_3 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=1,groups=1,bias_attr=False))
        self.conv34_4 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=1,groups=1,bias_attr=False))
        self.conv34_5 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=features,kernel_size=kernel_size,padding=1,groups=1,bias_attr=False))
        self.conv41 = nn.Sequential(nn.Conv2D(in_channels=features,out_channels=3,kernel_size=kernel_size,padding=padding,groups=groups,bias_attr=False))
        self.ReLU=nn.ReLU()
        self.upsample = ops.UpsampleBlock(64, scale=scale, multi_scale=multi_scale,group=1)
    def forward(self, x):
        x0 = self.sub_mean(x)
        x1 = self.conv1(x0)
        x1tcw = self.ReLU(x1)
        x2 = self.conv2(x1tcw)
        x3 = self.conv3(x2)
        c1 = paddle.concat([x1, x3], axis=1)
        c1 = self.ReLU(c1)
        x4 = self.conv4(c1)
        x5 = self.conv5(x4)
        c2 = paddle.concat([x3, x5], axis=1)
        c2 = self.ReLU(c2)
        x6 = self.conv6(c2)
        x7  = self.conv7(x6)
        c3 = paddle.concat([x5, x7], axis=1)
        c3 = self.ReLU(c3)
        x8 = self.conv8(c3)
        x9 = self.conv9(x8)
        c4 = paddle.concat([x7, x9], axis=1)
        c4 = self.ReLU(c4)
        x10 = self.conv10(c4)
        x11 = self.conv11(x10)
        c5 = paddle.concat([x9, x11], axis=1)
        c5 = self.ReLU(c5)
        x12 = self.conv12(c5)
        x13 = self.conv13(x12)
        c6 = paddle.concat([x11, x13], axis=1)
        c6 = self.ReLU(c6)
        x14 = self.conv14(c6)
        x15 = self.conv15(x14)
        c7 = paddle.concat([x13, x15], axis=1)
        c7 = self.ReLU(c7) 
        x16 = self.conv16(c7)
        x17 = self.conv17(x16)
        c7 = paddle.concat([x15, x17], axis=1)
        c7 = self.ReLU(c7)
        x18  = self.conv18(c7)
        x19 = self.conv19(x18)
        c8 = paddle.concat([x17, x19], axis=1)
        c8 = self.ReLU(c8)
        x20 = self.conv20(c8)
        x21 = self.conv21(x20)
        c9 = paddle.concat([x19, x21], axis=1)
        c9 = self.ReLU(c9)
        x22 = self.conv22(c9)
        x23  = self.conv23(x22)
        c10 = paddle.concat([x21, x23], axis=1)
        c10 = self.ReLU(c10)
        x24 = self.conv24(c10)
        x25 = self.conv25(x24)
        c11 = paddle.concat([x23, x25], axis=1)
        c11 = self.ReLU(c11)
        x26 = self.conv26(c11)
        x27 = self.conv27(x26)
        c12 = paddle.concat([x25, x27], axis=1)
        c12 = self.ReLU(c12)
        x28 = self.conv28(c12)
        x29 = self.conv29(x28)
        c13 = paddle.concat([x27, x29], axis=1)
        c13 = self.ReLU(c13)
        x30 = self.conv30(c13)
        x31 = self.conv31(x30)
        c14 = paddle.concat([x29, x31], axis=1)
        c14 = self.ReLU(c14) 
        x32 = self.conv32(c14)
        x33 = self.conv33(x32)
        c15 = paddle.concat([x31, x33], axis=1)
        c15 = self.ReLU(c15)
        x34  = self.conv34(c15)
        x34 = x1+x3+x5+x7+x9+x11+x13+x15+x17+x19+x21+x23+x25+x27+x29+x31+x33+x34
        x34 = self.ReLU(x34)
        x35  = self.conv35(x34)
        x36  = self.conv36(x35)
        x37  = self.conv37(x36)
        x38  = self.conv38(x37)
        x39  = self.conv39(x38)
        temp = self.upsample(x39, scale=self.scale)
        x111 = self.upsample(x1tcw,scale=self.scale)
        temp1 = x111+temp
        temp2 = self.ReLU(temp1)
        temp3 = self.conv34_1(temp2)
        temp3_1 = self.ReLU(temp3)
        temp4 = self.conv34_2(temp3_1)
        temp4_2 = self.ReLU(temp4)
        temp5 = self.conv34_3(temp4_2)
        temp5_2 = self.ReLU(temp5)
        temp6 = self.conv34_4(temp5_2)
        temp6_2 = self.ReLU(temp6)
        temp7 = self.conv34_5(temp6_2)
        temp7_1 = self.ReLU(temp7)
        x41 = self.conv41(temp7_1)
        out = self.add_mean(x41)
        return out
