<template>
  <div id="app">
   <v-app light>
    <v-toolbar color="white">
      <v-toolbar-title>Log</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn text @click="blogpage">Post</v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <v-content id="back">
      <section>
        <v-parallax src="http://file2.instiz.net/data/cached_img/upload/2016/05/09/23/7d931c39c52fe2837a5ec177e7223d36.jpg" height="650">
          <v-layout
            column
            align-center
            class="white--text"
          >
            <img src="./src/Untitled.png" alt="Vuetify.js" height="200">
            <h1 class="white--text mb-2 text-center" id="font">JunggoBi (중고비)</h1>
            <h1 class="subheading mb-4 text-center" id="main_font">저렴한 중고제품이 필요해!?</h1>
          </v-layout>
        </v-parallax>
      </section>

      <section>
        <v-layout
          column
          wrap
          class="my-12"
          align-center
        >
          <v-flex xs12 sm4 class="my-4">
            <div class="text-center">
              <center>
                <v-img src="./src/blue.png" width="25px"/>
              </center>
              <span id="font">The best way to find Ipad, Iphone, Galaxy...</span>
            </div>
          </v-flex>
          <v-flex xs12>
            <v-container grid-list-xl>
              <v-layout row wrap align-center>
                <v-flex xs12>
                  <v-card flat class="transparent">
                    <v-card-text class="text-center">
                      <!-- <v-icon x-large class="blue--text text--lighten-2">mdi-flash </v-icon> -->
                      <!-- <h1 id="font"> 필요한 게 뭐에요? </h1> -->
                      <search/>
                    </v-card-text>
                    <center>
                      <hr class="d-none d-lg-flex d-xl-none type_3">
                    </center>
                    <br/>
                    <br/>
                    <center>
                      <v-img src="./src/red.png" width="25px"/>
                    </center>
                    <detailsearch/>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
      </section>

      <section>
        <v-parallax src="http://file2.instiz.net/data/cached_img/upload/2016/05/09/23/dd22139d831d87ff1c2a096d5f42a400.jpg" height="500">
          <v-layout column align-center justify-center>
            <div class="white--text mb-4 text-center" id="main_font">가격이 이렇게까지 싸다고!?</div>
            <em id="font">가장 저렴한 제품 구경가기</em>
            <v-btn
              class="mt-12"
              color="blue lighten-2"
              dark
              large
              id="font"
              @click= "searchAll"
            >
            
              <!-- href="/pre-made-themes" -->
              최저가 보러가기
            </v-btn>
          </v-layout>
        </v-parallax>
      </section>

      <section>
        <v-container grid-list-xl>
          <v-layout row wrap justify-center class="my-12">
            <v-flex>
              <v-card flat class="transparent">
                <direct/>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
        <center>
          <hr class="d-none d-lg-flex d-xl-none type_3">
        </center>
        <br/>
      </section>

      <v-footer color="blue darken-2">
        <v-layout row wrap align-center>
          <v-flex xs12>
            <div class="white--text ml-4">
              Made with
              <v-icon class="red--text">mdi-heart</v-icon>
              by <a class="white--text" target="_blank">JunggoBi</a>
              and <a class="white--text" >Nuster, J-Bong, Jinsu, June</a>
            </div>
          </v-flex>
        </v-layout>
      </v-footer>
    </v-content>
  </v-app>
 </div>
</template>

<script>
const apiUrl = '/api'
import axios from "axios";
export default {
  methods: {
        async blogpage() {
            await this.$store.dispatch('data/getBlogPost').then(res => this.$router.push({ name :"BlogPage", params : { data : res}}));
        },
         async searchAll() {
      await this.$store.dispatch('data/searchById', "")
      .then(res => {
       
      })
    },

  }
}
</script>
<style scoped>
#font {
  font-family: 'Cute Font', cursive;
  font-size: 30px;
}
#main_font {
  font-family: 'Cute Font', cursive;
  font-size: 50px;
}
hr.type_3 {
  border: 0;
  height: 50px;
  width: 800px;
  background-image: url(Untitled1.png);
  background-repeat: no-repeat;
}
/* #back{
  background-color: #FDF7C0;
} */
</style>
