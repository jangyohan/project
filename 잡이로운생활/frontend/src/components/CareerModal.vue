<template>
  <transition name="modal">
    <div class="career-modal-mask" @mousedown.self="$emit('close')">
      <div class="career-modal-wrap">
        <div class="career-modal-content">
          <i class="fas fa-times" @click.self="$emit('close')"></i>
          <div>
            <p class="career-modal-head">경력기술서</p>
            <textarea v-model="careerDetail" readonly></textarea>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { mapState } from 'vuex';
import './css/career-modal.css'

export default {
  name: 'CareerModal',
  data() {
    return {
    }
  },
  watch: {
  },
  computed: {
    ...mapState(['careerDetail']),
  },
  created() {
  },
  methods: {

  }
}
</script>