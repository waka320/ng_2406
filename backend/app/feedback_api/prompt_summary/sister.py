class Sister:
    def __init__(self):
        pass

    def weather_feedback(self, weather):
        '''
        天気情報に対するフィードバックを生成するためのプロンプトを返す
        input(str) : weather
        output(str) : feedback
        '''
        prompt = (weather_data + "ここから本日の天気情報を取り出し、お姉さん口調で30字以内のアドバイスをください")
        return prompt

    def action_feedback(self, action):
        '''
        行動に対するフィードバックを生成するためのプロンプトを返す
        input(str) : action
        output(str) : feedback
        '''
        prompt = (
            f"{action}の行動で、うっかりしがちなポイント(特に忘れ物)をお姉さん口調で60字以内で教えてください。"
        )
        return prompt
    
    def gemini_error(self):
        '''
        エラーが起きた時に返すメッセージ
        input : None
        output : str : 怒っているメッセージ
        '''
        prompt = "ねえ！変なことしようとしてない！？ちゃんとした生活して！"
        return prompt