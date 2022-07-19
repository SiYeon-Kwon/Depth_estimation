해당 소스는 sparse-to-dense의 git을 인용하여 만들어진 코드입니다.
또한, fast-depth에서 mobilenet을 가져와 sparse-to-dense의 model.py 에 추가하였습니다.
model에 맞추어 개발 중이기 때문에, sparse-to-dense와 동일하지 않다는 점 유의해주시기 바랍니다.

#Make Dataset
NYUv2 데이터셋은 .h5확장자로 되어있습니다.
하지만 local에서는 이미지 확장자를 이용하여 Custom Dataset을 훈련을 시킬 예정입니다.
따라서 Custom Dataset을 만들기 위하여 Zed Camera 공식 홈페이지의 코드를 이용했고, 저장하는 부분을 만들어서 사용하였습니다.

#Make Dataset csv
이미지 데이터셋을 만들 때, train 폴더와 test 폴더 각각에 RGB와 Depth, 두 클래스가 있어야 합니다.
한 폴더 내에서 두 클래스를 분류해주어야 하기에 csv로 분류를 해주었고, 각각 train 폴더의 RGB, Depth와 test 폴더의 RGB, Depth로 csv 파일 두개를 만들었습니다.

csv를 읽어서 클래스를 분류하고 훈련이 가능토록 main.py에서 데이터를 불러올 때 csv를 읽을 수 있게 했고, 해당 코드에서는 Make Dataset로 만들어진 데이터셋을 csv로 변환하는 과정을 만들었습니다.