<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal_header">
            <div class="modal_header_text">Hashtag</div>
          </div>
          <div class="modal_close">
            <span class="modal_close_button" style="color:rgb(23, 196, 197)">
              <i class="fas fa-times-circle fa-2x" @click="$emit('close')"></i>
            </span>
          </div>

          <div class="modal_hash_body">
            <input
              class="modal_hash_body_write"
              placeholder="Hashtag를 작성해주세요"
              v-model="hashinput"
              @keyup.enter="hashadd"
            />

            <transition-group name="fade" tag="div" class="modal_hash_group">
              <div
                class="modal_hash_group_list"
                v-for="(hash, index) in hashList"
                :key="`hash-${index}`"
              >
                <div @click="delWriteHashItem(index)" class="modal_hash_close">
                  <i class="fas fa-times"></i>
                </div>
                {{ hash }}
              </div>
            </transition-group>
          </div>
          <div class="modal_footer_write">
            <button class="modal_footer_wirte_button" @click="onSubmit">추가하기</button>
            
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: "HashtagModal",
  data() {
    return {
      hashinput: "",
      hashList: [],
    };
  },
  methods: {
    hashadd() {
      this.hashList.push(this.hashinput);
      this.hashinput = "";
    },
    delWriteHashItem(index) {
      this.hashList.splice(index, 1);
    },
    onSubmit() {
      if (this.hashList == null || this.hashList == "") {
        alert("해쉬태그를 입력해주세요!");
      }
      else {
        this.$emit('on-hashtag', this.hashList)
        this.$emit('close')
      }
    },
  },
};
</script>

<style>
.modal_hash_body {
  margin-top: 5px;
  padding-right: 10px;
}
.modal_hash_body_write {
  margin-left: 5px;
  margin-bottom: 5px;
  width: 100%;
  border-radius: 10px;
  border-color: rgb(23, 196, 197);
  border-style:solid;
}
.modal_hash_body_write:focus {
  outline:none;
  border-color:rgb(23, 196, 197);
  
}

.modal_hash_group_list {
  display: inline-block;
  margin-right: 5px;

  margin-left: 5px;
  margin-bottom: 5px;
  border-radius: 5px;
  color: white;
  background-color: rgb(23, 196, 197);
  padding-left: 10px;
  padding-right: 10px;
}
.modal_hash_close {
  margin-right: 5px;
  display: inline;
}
.modal_hashtag_result {
  margin-top: 10px;
  width: 100%;
  resize: none;
}
</style>