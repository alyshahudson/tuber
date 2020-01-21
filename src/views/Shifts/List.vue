<template>
    <div>
      {{shifts}}
    </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'List',

  computed: {
    ...mapState('shifts', ['shifts']),
  },
};
</script>

<style scoped>

</style>
