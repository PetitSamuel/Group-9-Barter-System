<template>
  <section class="hero is-primary is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-3-widescreen">
            <form class="box">
              <div class="field">
                <label class="label">Name</label>
                <div class="control">
                  <input
                    v-model="name"
                    class="input"
                    type="text"
                    placeholder="Full Name"
                  />
                </div>
              </div>
              <div class="field">
                <label class="label">Username</label>
                <div class="control">
                  <input
                    v-model="username"
                    class="input"
                    type="text"
                    placeholder="Username"
                  />
                </div>
              </div>
              <div class="field">
                <label class="label">Password</label>
                <div class="control">
                  <input
                    v-model="password"
                    class="input"
                    type="password"
                    placeholder="********"
                  />
                </div>
              </div>
              <div class="field">
                <label class="label">Phone Number</label>
                <div class="control">
                  <input
                    v-model="phone"
                    class="input"
                    type="text"
                    placeholder="06..."
                  />
                </div>
              </div>
              <div class="field">
                <label class="label">Bio</label>
                <div class="control">
                  <textarea
                    v-model="bio"
                    class="input is-fullwidth"
                    type="text"
                    placeholder="Your bio..."
                  />
                </div>
              </div>
              <div v-if="errors.length" class="mb-3">
                <article class="message is-danger">
                  <div class="message-header">
                    <p v-for="error of errors" v-bind:key="error">
                      {{ error }}
                    </p>
                  </div>
                </article>
              </div>
              <div class="is-fullwidth">
                <button
                  type="button"
                  class="button is-primary is-fullwidth"
                  @click="register"
                >
                  Register
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import store from "@/store";

@Options({
  components: {},
  computed: {},
})
export default class Register extends Vue {
  username = "";
  password = "";
  name = "";
  phone = "";
  bio = "";
  errors: string[] = [];

  async register() {
    this.errors = [];
    if (!this.username) {
      this.errors.push("username cannot be empty");
    }
    if (!this.password) {
      this.errors.push("password cannot be empty");
    }
    if (!this.name) {
      this.errors.push("name cannot be empty");
    }
    if (!this.phone) {
      this.errors.push("phone cannot be empty");
    }

    if (this.errors.length === 0) {
      const username = this.username.trim();
      const password = this.password.trim();
      const name = this.name.trim();
      /* eslint-disable @typescript-eslint/camelcase */
      const phone_number = this.phone.trim();
      const bio = this.bio.trim();
      const resp = await store.dispatch("userStore/register", {
        username,
        password,
        name,
        bio,
        phone_number,
      });
      if (resp && resp["errors"]) {
        this.errors = resp["errors"].includes("403")
          ? ["Username already taken"]
          : ["An error occured"];
      }
    }
  }
}
</script>

<style>
textarea.input {
  height: 200px;
}
</style>
