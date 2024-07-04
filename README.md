このプログラムは以下の動作をします。  
This program implements the following tasks:  

1. [BoT-SORT](https://github.com/NirAharon/BoT-SORT)を使用してウミガメを追跡し、検出個体ごとにIDを付与する  
Tracking turtles using [BoT-SORT](https://github.com/NirAharon/BoT-SORT) and assigning IDs.  

-----------------------

BoT-SORT is released under the MIT license  
Copyright (c) 2022 Nir Aharon  

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  

-----------------------

2. YOLO v7を用いて検出個体の甲羅を検出する  
Detecting carapace using YOLO v7  

3. 甲羅の縦横比に応じてフィルタリング  
Filtering based on aspect ratio of the carapace  

4. 同一検出個体の画像の枚数に応じてフィルタリング  
Filtering based on the number of detected frames of an individual  


## 個体数推定のフロー  
## Instructions to estimate the number of individuals  

1. 自動検出したい動画を/videos/に入れる  
ドローンが発着する瞬間などはトリミングしておくと時間短縮・誤検出が減る  
Put a video file to analyze into /videos/  
Trimming video data (excluding irrelevant part for analysis such as departure) reduce time and false detections  


2. 以下のコマンドを入力することでBoT-SORTでの解析を開始（カメ全体の検出とMOT適用）  
出力結果は/runs/detect/に格納される  
--widthは動画の横幅（px）、--heightは動画の縦幅（px）  
Start analysis using BoT-SORT (detecting turtles and applying MOT) by the following command  
Output is stored in /runs/detect/  

`python botsort.py --weights pretrained/turtle.pt --source videos/test.mp4 --fuse-score --agnostic-nms --with-reid --save-txt --save-conf --width 3840 --height 2160`


3. 以下のコマンドを入力することでyolov7での解析を開始（カメの甲羅の検出）  
なお、コマンドを打つ前に/runs/detect/にcarapaceImgフォルダがないことを確認（あるとうまく動作しないので名前を変えたり削除しておく）  
コマンド内の --source runs/detect/exp/images は2で出力されたもののパスとする  
Start yolov7 (for detecting a turtle carapace) by the following command  
Confirm that there is no carapaceImg folder in /runs/detect/ before typing the command  
--source runs/detect/exp/images indicates path to output of 2  

`python detect_carapace.py --weights pretrained/carapace.pt --conf 0.25 --img-size 640 --source runs/detect/exp/images --name carapaceImg --save-txt --save-conf`

4. 以下のコマンドを入力することで縦横比によるフィルタリングを適用する  
縦横比の閾値を変更する場合は、--aspect_ratioの値を変える（default:0.5）  
Apply filtering based on the aspect ratio by the following command  
Threshold value can be changed by --aspect_ratio (default:0.5)  

`python aspect_filter.py --aspect_ratio 0.5`


5. 以下のコマンドを入力することでフォルダ内のファイルの枚数に応じてフィルタリングを行う  
（同一個体として検出したカメの検出枚数に応じてフィルタリング）  
削除するファイルの枚数の閾値を変更する場合は、--delete_numの値を変える（default:100 （100以下のフォルダは削除される））  
Apply filtering based on the number of detected frames of an individual   
Threshold value can be changed by --delete_num (default:100, folder(s) with 100 or less images are deleted)  

`python folder_filter.py --delete_num 100`


