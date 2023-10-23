css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #000000
}
.chat-message.bot {
    background-color: #000000
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
  }
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJiof3CT-nz8ElQFUnOjr7st1Lb6OKmNZhyQ&usqp=CAU" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="data:image/jpeg;base64,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">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''

