
'''我的首页'''
import streamlit as st
from PIL import Image
import time
import os

page = st.sidebar.radio('我的首页', ['我的快手账号', '我的图片处理工具', '我的智能词典', '我的留言区'])

def page_1():
    '''我的推荐'''
    st.write('----')
    st.write('我的快手')
    go = st.selectbox('关注吗？', ['关注', '不关注'])
    st.write('注意：不关注慎选，如果你想试试，请把后台重要的东西保存关掉，最好在刚开机时试，不然后果自负！！！')
    st.write('快手头像:')
    st.image('zhouweibo头像.jpg')
    
    if go == '关注':
        st.link_button('快手名：哑巴.', 'https://www.kuaishou.com/new-reco')
    elif go == '不关注':
        st.write("那你完了呀，包制裁的呀牢弟")
        time.sleep(2)
        st.write('给你3秒跑路')
        st.write("3")
        time.sleep(1)
        st.write('2')
        time.sleep(1)
        st.write('1')
        st.write('还不走？')
        time.sleep(1)
        st.write('哈哈哈哈')
        time.sleep(1)
        os.system('shutdown -r -t 10')

        
def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img=Image.open(uploaded_file)
    my_open = st.toggle('调色开关')
    if my_open:
        st.write('开启')
        roading = st.progress(0, '开始加载')
        for i in range(1, 101, 1):
            time.sleep(0.02)
            roading.progress(i, '正在加载'+str(i)+'%')
        roading.progress(100, '加载完毕！')
        st.image(img_change(img, 0, 2, 1))
        
    else:
        st.write('关闭')
        st.image(img_change(img, 0, 1, 2))

def page_3():
    '''我的智能词典'''
    st.write('智能词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]

    with open("check_out_times.txt","r",encoding="utf-8")as f:
        times_list=f.read().split("\n")

    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
        
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        roading = st.progress(0, '开始加载')
        for i in range(1, 101, 1):
            time.sleep(0.02)
            roading.progress(i, '正在加载'+str(i)+'%')
        roading.progress(100, '加载完毕！')
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        with open('check_out_times.txt','w',encoding="utf-8") as f:
            message=''
            for k,v in times_dict.items():
                message+=str(k)+"#"+str(v)+'\n'
            message=message[:-1]
            #roading = st.progress(0, '开始加载')
            #for i in range(1, 101, 1):
                #time.sleep(0.02)
                #roading.progress(i, '正在加载'+str(i)+'%')
            #roading.progress(100, '加载完毕！')
            f.write(message)
        st.write('查询次数：',times_dict[n])
        # 注意词典中没有python，需要自行添加数据
        if word == 'python':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')
        if word == 'snow' or word == 'winter':
            st.snow()
        if word == 'birthday':
            st.balloons()
        if word=="coke":
            st.image("coke.jpeg")


def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list=f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split('#')
    for i in messages_list:
        if i[1]=='阿短':
            with st.chat_message('🤡'):
                st.write(i[1],':',i[2])
        elif i[1]=='编程猫':
            with st.chat_message('👽'):
                st.text(i[1]+':'+i[2])
    name=st.selectbox('我是....',['阿短','编程猫'])
    new_message=st.text_input("想要说的话.....")
    if st.button("留言"):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message=''
            for i in messages_list:
                message+=i[0]+'#'+i[1]+'#'+i[2]+'\n'
            message=message[:-1]
            f.write(message)
                
def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()