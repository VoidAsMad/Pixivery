from pixivery.http import PixivRequest

class Pixiv(PixivRequest):
  def __init__(self):
    pass

  def get_artwork(self, id : str):
    tag = ['artwork' , id]
    result = self.requests(tag)
    return result

  def get_ranking(self, mode : str = 'daily', limit : int = None):
    tag = ['rank', mode, limit]
    result = self.requests(tag)
    return result
