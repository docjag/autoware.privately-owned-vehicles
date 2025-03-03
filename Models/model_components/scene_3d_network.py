from .scene_3d_upstream import Scene3DUpstream
from .scene_3d_neck import Scene3DNeck
from .scene_3d_head import Scene3DHead

import torch.nn as nn

class Scene3DNetwork(nn.Module):
    def __init__(self, pretrained):
        super(Scene3DNetwork, self).__init__()

        # Upstream blocks
        self.Scene3DUpstream = Scene3DUpstream(pretrained)

        # Neck
        self.DepthNeck = Scene3DNeck()

        # Depth Head
        self.SuperDepthHead = Scene3DHead()
    

    def forward(self, image):
        context, features = self.Scene3DUpstream(image)
        neck = self.DepthNeck(context, features)
        prediction = self.SuperDepthHead(neck, features)
        return prediction