<template>
  <div>
    <br>
    <v-card max-width="1000px" class="mx-auto" :raised="true">
        <v-card-title>
            Hotel Room Requests
        </v-card-title>
        <v-card-text>
            <v-data-table :headers="headers" :items="requests">
                <template v-slot:item.room_nights="{ item }">
                    <div v-for="night in room_nights" :key="night.id">
                        <v-chip small style="cursor: pointer" v-if="night.restricted && Object.prototype.hasOwnProperty.call(item.room_nights, night.id.toString()) && item.room_nights[night.id.toString()].requested" @click="approve(item.room_nights[night.id.toString()], department.id)">
                        <v-icon left>{{ item.room_nights[night.id.toString()].approved ? "check" : item.room_nights[night.id.toString()].approved===false ? "clear" : "check_box_outline_blank" }}</v-icon>
                        {{ night.name }}
                        </v-chip>
                    </div>
                    </template>
                    <template v-slot:item.name="{ item }">
                    <div v-if="checkPermission('hotel_assignment.read')">
                        <router-link :to="{name: 'hotelsrequestview', params: {badge: item.id}}">
                        {{ item.name }}
                        </router-link>
                    </div>
                    <div v-else>
                        {{ item.name }}
                    </div>
                </template>
            </v-data-table>
        </v-card-text>
    </v-card>
  </div>
</template>

<style>
</style>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'RequestApprove',
  components: {
  },
  data: () => ({
    loading: false,
    headers: [
      {
        text: 'Name',
        value: 'name',
      },
      {
        text: 'Departments',
        value: 'departments',
      },
      {
        text: 'Declined',
        value: 'declined',
      },
      {
        text: 'Requested Nights',
        value: 'room_nights_requested',
      },
      {
        text: 'Approved Nights',
        value: 'room_nights_approved',
      },
      {
        text: 'Assigned Nights',
        value: 'room_nights_assigned',
      },
      {
        text: 'Roommate Requests',
        value: 'requested_roommates',
      },
      {
        text: 'Roommate Anti-Requests',
        value: 'antirequested_roommates',
      },
      {
        text: 'Justification',
        value: 'justification',
      },
      {
        text: 'Notes',
        value: 'notes',
      },
    ],
  }),
  computed: {
    ...mapGetters([
      'event',
      'user',
    ]),
    requests() {
      return [];
    },
  },
  asyncComputed: {
    roommates() {

    },
    departments() {
      const self = this;
      return new Promise((resolve) => {
        if (self.event.id && self.user.id) {
          self.get('/api/hotels/requests', {
            event: self.event.id,
            user: self.user.id,
          }).then((depts) => {
            if (depts.success) {
              resolve(depts.departments);
            } else {
              resolve([]);
            }
          }).catch(() => {
            self.$store.commit('open_snackbar', 'Failed to load hotel request.');
          });
        } else {
          resolve([]);
        }
      });
    },
    room_nights() {
      const self = this;
      return new Promise((resolve) => {
        if (self.event.id) {
          self.get('/api/hotels/room_nights', {
            event: self.event.id,
          }).then((res) => {
            if (res.success) {
              resolve(res.room_nights);
            } else {
              resolve([]);
            }
          }).catch(() => {
            self.$store.commit('open_snackbar', 'Failed to load room nights.');
          });
        } else {
          resolve([]);
        }
      });
    },
  },
  mounted() {
  },
  methods: {
  },
};
</script>
