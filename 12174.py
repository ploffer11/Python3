"""for i in range(int(input())):
    byte = 8
    input()
    arr = input().replace("O", "0").replace("I", "1")
    decode = [
        chr(int(arr[i*byte : i*byte + byte], 2))
        for i in range(len(arr)//byte)
    ]
    print(f"Case #{i+1}:","".join(decode))
"""

j=1;p=str.replace;r=input;k=lambda:int(r());exec('l=k();a=p(p(r(),"O","0"),"I","1");print(f"Case #{j}:","".join([chr(int(a[i*8:i*8+8],2))for i in range(l)]));j+=1;'*k())