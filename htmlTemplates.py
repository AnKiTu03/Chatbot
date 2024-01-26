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
        <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Femojiisland.com%2Fproducts%2Fman-emoji-unknown&psig=AOvVaw2WrNPAS3klvKCXjef-uGLV&ust=1706341944948000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCLiv3KLJ-oMDFQAAAAAdAAAAABAD">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
