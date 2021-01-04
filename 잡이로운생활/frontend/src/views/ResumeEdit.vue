<template>
  <div class="wrap">
    <div class="wrap-container">
      <div class="resume-edit-save-btn-box">
        <div class="resume-edit-save-btn" @click="editResume">저장하기</div>
      </div>
      <div class="resume-edit-box resume-edit-user-box">
        <p>개인정보</p>
        <div class="resume-edit-user-content">
          <label for="resume-edit-user-img-edit">
            <div class='resume-edit-user-img-box'>
                <i v-if="!getData.image" class="far fa-images"><i class="fas fa-plus"></i></i>
                <input type="file" id="resume-edit-user-img-edit" accept="image/*" @change="setProfileImg">
              <p v-if="!getData.image">프로필 사진을 등록해주세요</p>
              <img v-if='getData.image' class="resume-edit-user-img" :src="getData.image" alt="#">
            </div>
          </label>
          <div class="resume-edit-user-profile">
            <div class="resume-edit-user-name-box resume-edit-user-profile-box">
              <span>이름</span>
              <input v-model="getData.name" type="text" class="resume-edit-user-input">
            </div>
            <div class="resume-edit-user-birth-box resume-edit-user-profile-box">
              <span>생년월일</span>
              <input v-model="getData.date_of_birth" type="text" class="resume-edit-user-input">
            </div>
            <div class="resume-edit-user-mail-box resume-edit-user-profile-box">
              <span>이메일</span>
              <input v-model="getData.email" type="text" class="resume-edit-user-input">
            </div>
            <div class="resume-edit-user-num-box resume-edit-user-profile-box">
              <span>휴대폰</span>
              <input v-model="getData.phone_number" type="text" class="resume-edit-user-input">
            </div>
          </div>
        </div>
      </div>

      <div class="resume-edit-box resume-edit-army-box">
        <p>병역사항</p>
        <div class="resume-edit-license-content">
          <div class="resume-edit-army-input-box resume-edit-input-box">
            <div class="resume-edit-input-inner-box resume-edit-army-inner-box">
              <div class="inner-box army-sort-input">
                <label for="army-sort">병역구분</label>
                <select v-model='getData.military_classification' name="sort" id="army-sort">
                  <option disabled selected>선택</option>
                  <option>군필</option><option>면제</option><option>미필</option>
                  <option>복무중</option><option>비대상(여성)</option>
                </select>
              </div>
              <div class="inner-box army-ability-input">
                <label for="">군별</label>
                <input v-model="getData.military_branch" type="text" v-on:input="getData.military_branch = $event.target.value">
              </div>
              <div class="inner-box army-rank-input">
                <label for="">계급</label>
                <input v-model="getData.military_rank" type="text" v-on:input="getData.military_rank = $event.target.value">
              </div>
            </div>
            <div class="resume-edit-input-inner-box resume-edit-army-inner-box">
              <div class="inner-box army-discharge-input">
                <label for="army-discharge">제대구분</label>
                <select v-model='getData.military_completed' name="discharge" id="army-discharge">
                  <option disabled selected>선택</option>
                  <option>만기제대</option><option>소집해제</option><option>의가사제대</option>
                  <option>의병제대</option><option>불명예제대</option><option>상이제대</option>
                </select>
              </div>
              <div class="inner-box army-reson-input">
                <label for="">면제사유</label>
                <input v-model="getData.military_completed_reason" type="text" v-on:input="getData.military_completed_reason = $event.target.value">
              </div>
              <div class="inner-box army-date-input">
                <label for="">복무기간</label>
                <input type="text" v-model='getData.military_start' placeholder="YYYY . MM"><span>~</span>
                <input type="text" v-model='getData.military_end' placeholder="YYYY . MM">
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="resume-edit-box resume-edit-school-box">
        <p>학력사항</p>
        <div class="resume-edit-license-content">
          <div class="resume-edit-license-certify-box">
            <p v-if="(certifiedSchool[0].length+certifiedSchool[1].length+certifiedSchool[2].length
            +certifiedSchool[3].length+certifiedSchool[4].length)===0">인증된 학력이 없습니다.</p>
            <div class='resume-edit-license-list-box' v-for='(certified, index) in certifiedSchool' :key='`certified-${index}`'>
              <div class="resume-edit-license-certified-list" v-if="certified[0]">
                <div class="certified-detail certified-type">{{ certified[0] }}</div>
                <div class="certified-detail">{{ certified[1] }}</div><div class="certified-detail">{{ certified[2] }}</div>
                <div class="certified-detail">{{ certified[3] }}</div><div class="certified-detail certified-detail-non-margin">{{ certified[4] }}</div>
                <div class="certified-detail certified-detail-non-margin">~</div><div class="certified-detail">{{ certified[5] }}</div>
                <div v-if="certified[6]" class="certified-detail certified-detail-non-margin">{{ certified[6] }}</div>
                <div v-if="certified[6]" class="certified-detail certified-detail-non-margin">/</div>
                <div v-if="certified[7]" class="certified-detail">{{ certified[7] }}</div>
                <div v-if="certified[8]" class="certified-detail certified-detail-non-margin">{{ certified[8] }}</div>
                <div v-if="certified[8]" class="certified-detail certified-detail-non-margin">/</div><div v-if="certified[9]" class="certified-detail">{{ certified[9] }}</div>
                <div class="certified-detail certified-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                <div class="certified-detail certified-del-box" @click="delSchool(certified[0])">x</div>
              </div>
            </div>
          </div>
          <div class="resume-edit-license-school-box">
            <div class="resume-edit-license-school-btn high-school-btn" @click="onHighSchool">고등학교</div>
            <div class="resume-edit-license-school-btn tec-univ-btn" @click="onTecUniv">전문대학</div>
            <div class="resume-edit-license-school-btn univ-btn" @click="onUniv">대학교</div>
            <div class="resume-edit-license-school-btn master-btn" @click="onMaster">석사</div>
            <div class="resume-edit-license-school-btn doctor-btn" @click="onDoctor">박사</div>
          </div>

          <div v-if="isHighSchool" class="resume-edit-license-high-school-input-box resume-edit-input-box">
            <div class="resume-edit-input-inner-box">
              <div class="inner-box school-name-input">
                <label for="">학교명</label>
                <input v-model="getData.highschool_name" type="text" v-on:input="getData.highschool_name = $event.target.value" @keydown.enter="onModal('high_list', getData.highschool_name, 0, 'high')">
                <i class="fab fa-sistrix" @click="onModal('high_list', getData.highschool_name, 0, 'high')"></i>
              </div>
              <div class="inner-box graduate-select-input">
                <label for="gradu-combo">졸업구분</label>
                <select v-model='getData.highschool_classification' name="graduation" id="gradu-combo">
                  <option disabled selected>선택</option>
                  <option>졸업</option><option>졸업예정</option>
                  <option>중퇴</option><option>수료</option><option>재학</option>
                </select>
              </div>
              <div class="inner-box location-input">
                <label for="school-location">소재지</label>
                <select v-model='getData.highschool_location' name="location" id="school-location">
                  <option disabled selected>선택</option>
                  <option>서울</option><option>인천</option><option>부산</option>
                  <option>대전</option><option>대구</option><option>광주</option>
                  <option>울산</option><option>강원</option><option>경기</option>
                  <option>경남</option><option>경북</option><option>전남</option>
                  <option>전북</option><option>충남</option><option>충북</option><option>제주</option>
                </select>
              </div>
            </div>
            <div class="resume-edit-input-inner-box">
              <div class="inner-box entrance-date-input">
                <label for="">입학년월</label><input type="text" v-model='getData.highschool_entrance_year' placeholder="YYYY . MM">
              </div>
              <div class="inner-box graduation-date-input">
                <label for="">졸업년월</label><input type="text" v-model='getData.highschool_graduation_year' placeholder="YYYY . MM">
              </div>
            </div>
          </div>

          <div v-if="isTecUniv" class="resume-edit-license-tec-univ-input-box resume-edit-input-box">
            <div class="resume-edit-input-inner-box">
              <div class="inner-box school-name-input">
                <label for="">학교명</label>
                <input v-model="getData.college_name" type="text" v-on:input="getData.college_name = $event.target.value" @keydown.enter="onModal('univ_list', getData.college_name, 100322, 'tecUniv')">
                <i class="fab fa-sistrix" @click="onModal('univ_list', getData.college_name, 100322, 'tecUniv')"></i>
              </div>
              <div class="inner-box graduate-select-input">
                <label for="">졸업구분</label>
                <select v-model='getData.college_classification' name="graduation" id="gradu-combo">
                  <option disabled selected>선택</option>
                  <option>졸업</option><option>졸업예정</option>
                  <option>중퇴</option><option>수료</option><option>재학</option>
                </select>
              </div>
              <div class="inner-box location-input">
                <label for="">소재지</label>
                <select v-model='getData.college_location' name="location" id="school-location">
                  <option disabled selected>선택</option>
                  <option>서울</option><option>인천</option><option>부산</option>
                  <option>대전</option><option>대구</option><option>광주</option>
                  <option>울산</option><option>강원</option><option>경기</option>
                  <option>경남</option><option>경북</option><option>전남</option>
                  <option>전북</option><option>충남</option><option>충북</option><option>제주</option>
                </select>
              </div>
            </div>
            <div class="resume-edit-input-inner-box">
              <div class="inner-box entrance-date-input">
                <label for="">입학년월</label><input type="text" v-model='getData.college_entrance_year' placeholder="YYYY . MM">
              </div>
              <div class="inner-box graduation-date-input">
                <label for="">졸업년월</label><input type="text" v-model='getData.college_graduation_year' placeholder="YYYY . MM">
              </div>
            </div>
            <div class="resume-edit-input-inner-box">
              <div class="inner-box major-name-input">
                <label for="">전공</label>
                <input type="text" v-model="getData.college_major" v-on:input="getData.college_major = $event.target.value" @keydown.enter="onModal2(getData.college_major, 'tecUniv', 'major')">
                <i class="fab fa-sistrix" @click="onModal2(getData.college_major, 'tecUniv', 'major')"></i>
              </div>
              <div class="inner-box minor-name-input">
                <label for="">부전공</label>
                <input type="text" v-model="getData.college_minor" v-on:input="getData.college_minor = $event.target.value" @keydown.enter="onModal2(getData.college_minor, 'tecUniv', 'minor')">
                <i class="fab fa-sistrix" @click="onModal2(getData.college_minor, 'tecUniv', 'minor')"></i>
              </div>
              <div class="inner-box grade-input">
                <label for="">학점</label>
                <input type="text" placeholder="학점"  v-model="getData.college_grade">
                <select name="total-grade" id="grade-combo" v-model="getData.college_total">
                  <option disabled selected>선택</option>
                  <option>4</option><option>4.3</option><option>4.5</option>
                </select>
              </div>
            </div>
          </div>
          <div v-if="isUniv" class="resume-edit-license-univ-input-box resume-edit-input-box">
            <div class="resume-edit-input-inner-box">
              <div class="inner-box school-name-input">
                <label for="">학교명</label>
                <input v-model="getData.university_name" type="text" v-on:input="getData.university_name = $event.target.value" @keydown.enter="onModal('univ_list', getData.university_name, 100323, 'univ')">
                <i class="fab fa-sistrix" @click="onModal('univ_list', getData.university_name, 100323, 'univ')"></i>
              </div>
              <div class="inner-box graduate-select-input">
                <label for="">졸업구분</label>
                <select v-model='getData.university_classification' name="graduation" id="gradu-combo">
                  <option disabled selected>선택</option>
                  <option>졸업</option><option>졸업예정</option>
                  <option>중퇴</option><option>수료</option><option>재학</option>
                </select>
              </div>
              <div class="inner-box location-input">
                <label for="">소재지</label>
                <select v-model='getData.university_location' name="location" id="school-location">
                  <option disabled selected>선택</option>
                  <option>서울</option><option>인천</option><option>부산</option>
                  <option>대전</option><option>대구</option><option>광주</option>
                  <option>울산</option><option>강원</option><option>경기</option>
                  <option>경남</option><option>경북</option><option>전남</option>
                  <option>전북</option><option>충남</option><option>충북</option><option>제주</option>
                </select>
              </div>
            </div>
            <div class="resume-edit-input-inner-box">
              <div class="inner-box entrance-date-input">
                <label for="">입학년월</label><input type="text" v-model='getData.university_entrance_year' placeholder="YYYY . MM">
              </div>
              <div class="inner-box graduation-date-input">
                <label for="">졸업년월</label><input type="text" v-model='getData.university_graduation_year' placeholder="YYYY . MM">
              </div>
            </div>
            <div class="resume-edit-input-inner-box">
              <div class="inner-box major-name-input">
                <label for="">전공</label>
                <input type="text" v-model="getData.university_major" v-on:input="getData.university_major = $event.target.value" @keydown.enter="onModal2(getData.university_major, 'univ', 'major')">
                <i class="fab fa-sistrix" @click="onModal2(getData.university_major, 'univ', 'major')"></i>
              </div>
              <div class="inner-box minor-name-input">
                <label for="">부전공</label>
                <input type="text" v-model="getData.university_minor" v-on:input="getData.university_minor = $event.target.value" @keydown.enter="onModal2(getData.university_minor, 'univ', 'minor')">
                <i class="fab fa-sistrix" @click="onModal2(getData.university_minor, 'univ', 'minor')"></i>
              </div>
              <div class="inner-box grade-input">
                <label for="">학점</label>
                <input type="text" placeholder="학점"  v-model="getData.university_grade">
                <select name="total-grade" id="grade-combo" v-model="getData.university_total">
                  <option disabled selected>선택</option>
                  <option>4</option><option>4.3</option><option>4.5</option>
                </select>
              </div>
            </div>
          </div>
          <div v-if="isMaster" class="resume-edit-license-master-input-box resume-edit-input-box">
            <div class="resume-edit-input-inner-box">
              <div class="inner-box school-name-input">
                <label for="">학교명</label>
                <input v-model="getData.master_name" type="text" v-on:input="getData.master_name = $event.target.value" @keydown.enter="onModal('univ_list', getData.master_name, 100323, 'master')">
                <i class="fab fa-sistrix" @click="onModal('univ_list', getData.master_name, 100323, 'master')"></i>
              </div>
              <div class="inner-box graduate-select-input">
                <label for="">졸업구분</label>
                <select v-model='getData.master_classification' name="graduation" id="gradu-combo">
                  <option disabled selected>선택</option>
                  <option>졸업</option><option>졸업예정</option>
                  <option>중퇴</option><option>수료</option><option>재학</option>
                </select>
              </div>
              <div class="inner-box location-input">
                <label for="">소재지</label>
                <select v-model='getData.master_location' name="location" id="school-location">
                  <option disabled selected>선택</option>
                  <option>서울</option><option>인천</option><option>부산</option>
                  <option>대전</option><option>대구</option><option>광주</option>
                  <option>울산</option><option>강원</option><option>경기</option>
                  <option>경남</option><option>경북</option><option>전남</option>
                  <option>전북</option><option>충남</option><option>충북</option><option>제주</option>
                </select>
              </div>
            </div>
            <div class="resume-edit-input-inner-box">
              <div class="inner-box entrance-date-input">
                <label for="">입학년월</label><input type="text" v-model='getData.master_entrance_year' placeholder="YYYY . MM">
              </div>
              <div class="inner-box graduation-date-input">
                <label for="">졸업년월</label><input type="text" v-model='getData.master_graduation_year' placeholder="YYYY . MM">
              </div>
            </div>
            <div class="resume-edit-input-inner-box">
              <div class="inner-box major-name-input">
                <label for="">전공</label>
                <input type="text" v-model="getData.master_major" v-on:input="getData.master_major = $event.target.value" @keydown.enter="onModal2(getData.master_major, 'master', 'major')">
                <i class="fab fa-sistrix" @click="onModal2(getData.master_major, 'master', 'major')"></i>
              </div>
              <div class="inner-box minor-name-input">
                <label for="">부전공</label>
                <input type="text" v-model="getData.master_minor" v-on:input="getData.master_minor = $event.target.value" @keydown.enter="onModal2(getData.master_minor, 'master', 'minor')">
                <i class="fab fa-sistrix" @click="onModal2(getData.master_minor, 'master', 'minor')"></i>
              </div>
              <div class="inner-box grade-input">
                <label for="">학점</label>
                <input type="text" placeholder="학점"  v-model="getData.master_grade">
                <select name="total-grade" id="grade-combo" v-model="getData.master_total">
                  <option disabled selected>선택</option>
                  <option>4</option><option>4.3</option><option>4.5</option>
                </select>
              </div>
            </div>
          </div>
          <div v-if="isDoctor" class="resume-edit-license-doctor-input-box resume-edit-input-box">
            <div class="resume-edit-input-inner-box">
              <div class="inner-box school-name-input">
                <label for="">학교명</label>
                <input v-model="getData.doctor_name" type="text" v-on:input="getData.doctor_name = $event.target.value" @keydown.enter="onModal('univ_list', getData.doctor_name, 100323, 'doctor')">
                <i class="fab fa-sistrix" @click="onModal('univ_list', getData.doctor_name, 100323, 'doctor')"></i>
              </div>
              <div class="inner-box graduate-select-input">
                <label for="">졸업구분</label>
                <select v-model='getData.doctor_classification' name="graduation" id="gradu-combo">
                  <option disabled selected>선택</option>
                  <option>졸업</option><option>졸업예정</option>
                  <option>중퇴</option><option>수료</option><option>재학</option>
                </select>
              </div>
              <div class="inner-box location-input">
                <label for="">소재지</label>
                <select v-model='getData.doctor_location' name="location" id="school-location">
                  <option disabled selected>선택</option>
                  <option>서울</option><option>인천</option><option>부산</option>
                  <option>대전</option><option>대구</option><option>광주</option>
                  <option>울산</option><option>강원</option><option>경기</option>
                  <option>경남</option><option>경북</option><option>전남</option>
                  <option>전북</option><option>충남</option><option>충북</option><option>제주</option>
                </select>
              </div>
            </div>
            <div class="resume-edit-input-inner-box">
              <div class="inner-box entrance-date-input">
                <label for="">입학년월</label><input type="text" v-model='getData.doctor_entrance_year' placeholder="YYYY . MM">
              </div>
              <div class="inner-box graduation-date-input">
                <label for="">졸업년월</label><input type="text" v-model='getData.doctor_graduation_year' placeholder="YYYY . MM">
              </div>
            </div>
            <div class="resume-edit-input-inner-box">
              <div class="inner-box major-name-input">
                <label for="">전공</label>
                <input type="text" v-model="getData.doctor_major" v-on:input="getData.doctor_major = $event.target.value" @keydown.enter="onModal2(getData.doctor_major, 'doctor', 'major')">
                <i class="fab fa-sistrix" @click="onModal2(getData.doctor_major, 'doctor', 'major')"></i>
              </div>
              <div class="inner-box minor-name-input">
                <label for="">부전공</label>
                <input type="text" v-model="getData.doctor_minor" v-on:input="getData.doctor_minor = $event.target.value" @keydown.enter="onModal2(getData.doctor_minor, 'doctor', 'minor')">
                <i class="fab fa-sistrix" @click="onModal2(getData.doctor_minor, 'doctor', 'minor')"></i>
              </div>
              <div class="inner-box grade-input">
                <label for="">학점</label>
                <input type="text" placeholder="학점"  v-model="getData.doctor_grade">
                <select name="total-grade" id="grade-combo" v-model="getData.doctor_total">
                  <option disabled selected>선택</option>
                  <option>4</option><option>4.3</option><option>4.5</option>
                </select>
              </div>
            </div>
          </div>
          <div class="resume-edit-license-btn-box resume-edit-input-box">
            <div v-if="formHighSchool" class="resume-edit-license-btn  on-license-btn" @click="addSchool('high')">인증하기</div>
            <div v-if="formTecUniv" class="resume-edit-license-btn  on-license-btn" @click="addSchool('tecUniv')">인증하기</div>
            <div v-if="formUniv" class="resume-edit-license-btn  on-license-btn" @click="addSchool('univ')">인증하기</div>
            <div v-if="formMaster" class="resume-edit-license-btn  on-license-btn" @click="addSchool('master')">인증하기</div>
            <div v-if="formDoctor" class="resume-edit-license-btn  on-license-btn" @click="addSchool('doctor')">인증하기</div>
            <div v-if="!isSchool" class="resume-edit-license-btn">인증하기</div>
          </div>
        </div>
      </div>

      
      <div class="resume-edit-box resume-edit-license-box">
        <p>자격사항</p>
        <div class="resume-edit-license-content">
          <div class="resume-edit-license-certify-box">
            <p v-if="(getLicense.length+certifiedLicense.length)===0">인증된 자격증이 없습니다.</p>
            <div class='resume-edit-license-list-box' v-for='(license, index) in getLicense' :key='`license1-${index}`'>
              <div class="resume-edit-license-certified-list" v-if="license.name">
                <div class="certified-detail certified-type">{{ license.name }}</div>
                <div class="certified-detail">{{ license.publisher }}</div><div class="certified-detail">{{ license.date }}</div>
                <div class="certified-detail certified-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                <div class="certified-detail certified-del-box" @click="delLicense('certified', license.id, index)">x</div>
              </div>
            </div>
            <div class='resume-edit-license-list-box' v-for='(license, index) in certifiedLicense' :key='`license2-${index}`'>
              <div class="resume-edit-license-certified-list" v-if="license[0]">
                <div class="certified-detail certified-type">{{ license[0] }}</div>
                <div class="certified-detail">{{ license[1] }}</div><div class="certified-detail">{{ license[2] }}</div>
                <div class="certified-detail certified-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                <div class="certified-detail certified-del-box" @click="delLicense('tmp', null, index)">x</div>
              </div>
            </div>
          </div>
          <div class="resume-edit-license-input-box resume-edit-input-box">
            <div class="resume-edit-input-inner-box resume-edit-license-inner-box">
              <div class="inner-box license-name-input">
                <label for="">자격증명</label>
                <input v-model="license.name" type="text" v-on:input="license.name = $event.target.value">
              </div>
              <div class="inner-box graduate-select-input">
                <label for="gradu-combo">발행처</label>
                <input v-model="license.institute" type="text" v-on:input="license.institute = $event.target.value">
              </div>
              <div class="inner-box entrance-date-input">
                <label for="">취득일</label><input type="text" v-model='license.date' placeholder="YYYY . MM">
              </div>
            </div>
          </div>
          <div class="resume-edit-license-btn-box resume-edit-input-box">
            <div v-if="isLicense" class="resume-edit-license-btn  on-license-btn" @click="addLicense">인증하기</div>
            <div v-if="!isLicense" class="resume-edit-license-btn">인증하기</div>
          </div>
        </div>
      </div>

      <div class="resume-edit-box resume-edit-lang-box">
        <p>어학사항</p>
        <div class="resume-edit-license-content">
          <div class="resume-edit-license-certify-box">
            <p v-if="(getLang.length+certifiedLang.length)===0">인증된 어학성적이 없습니다.</p>
            <div class='resume-edit-license-list-box' v-for='(lang, index) in getLang' :key='`lang1-${index}`'>
              <div class="resume-edit-license-certified-list" v-if="lang.classification">
                <div class="certified-detail certified-type">{{ lang.classification }}</div>
                <div class="certified-detail">{{ lang.name }}</div><div class="certified-detail">{{ lang.score }}</div>
                <div class="certified-detail">{{ lang.date }}</div>
                <div class="certified-detail certified-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                <div class="certified-detail certified-del-box" @click="delLang('certified', lang.id, index)">x</div>
              </div>
            </div>
            <div class='resume-edit-license-list-box' v-for='(lang, index) in certifiedLang' :key='`lang2-${index}`'>
              <div class="resume-edit-license-certified-list" v-if="lang[0]">
                <div class="certified-detail certified-type">{{ lang[0] }}</div>
                <div class="certified-detail">{{ lang[1] }}</div><div class="certified-detail">{{ lang[2] }}</div>
                <div class="certified-detail">{{ lang[3] }}</div>
                <div class="certified-detail certified-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                <div class="certified-detail certified-del-box" @click="delLang('tmp', null, index)">x</div>
              </div>
            </div>
          </div>
          <div class="resume-edit-lang-input-box resume-edit-input-box">
            <div class="resume-edit-input-inner-box resume-edit-lang-inner-box">
              <div class="inner-box lang-name-input">
                <label for="lang-sort">언어</label>
                <select v-model='lang.sort' name="sort" id="lang-sort">
                  <option disabled selected>선택</option>
                  <option>영어</option><option>중국어</option><option>일본어</option>
                  <option>러시아어</option><option>스페인어</option><option>프랑스어</option>
                  <option>독일어</option><option>한국어</option><option>베트남어</option>
                </select>
              </div>
              <div class="inner-box lang-name-input">
                <label for="">시험명</label>
                <input v-model="lang.name" type="text" v-on:input="lang.name = $event.target.value">
              </div>
              <div class="inner-box lang-rank-input">
                <label for="">점수</label>
                <input v-model="lang.rank" type="text" v-on:input="lang.rank = $event.target.value">
              </div>
              <div class="inner-box lang-date-input">
                <label for="">취득일</label><input type="text" v-model='lang.date' placeholder="YYYY . MM">
              </div>
            </div>
          </div>
          <div class="resume-edit-license-btn-box resume-edit-input-box">
            <div v-if="isLang" class="resume-edit-license-btn  on-license-btn" @click="addLang">인증하기</div>
            <div v-if="!isLang" class="resume-edit-license-btn">인증하기</div>
          </div>
        </div>
      </div>

      <div class="resume-edit-box resume-edit-career-box">
        <p>경력사항</p>
        <div class="resume-edit-license-content">
          <div class="resume-edit-license-certify-box">
            <p v-if="(certifiedCareer.length+getCareer.length)===0">인증된 경력이 없습니다.</p>
            <div class='resume-edit-license-list-box' v-for='(career, index1) in getCareer' :key='`career1-${index1}`'>
              <div class="resume-edit-license-certified-list" v-if="career.name">
                <div class="certified-detail certified-type">{{ career.name }}</div>
                <div class="certified-detail certified-detail-non-margin">{{ career.start_term }}</div>
                <div class="certified-detail certified-detail-non-margin">~</div>
                <div class="certified-detail">{{ career.end_term }}</div>
                <div class="certified-detail">{{ career.retirement_reason }}</div><div class="certified-detail">{{ career.department }}</div>
                <div class="certified-detail">{{ career.rank }}</div><div class="certified-detail">{{ career.duty }}</div>
                <div class="certified-detail certified-detail-career-text" @click="onModal3(career.statement)">
                  경력기술서
                </div>
                <div class="certified-detail certified-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                <div class="certified-detail certified-del-box" @click="delCareer('certified', career.id, index1)">x</div>
              </div>
            </div>
            <div class='resume-edit-license-list-box' v-for='(career, index2) in certifiedCareer' :key='`career2-${index2}`'>
              <div class="resume-edit-license-certified-list" v-if="career[0]">
                <div class="certified-detail certified-type">{{ career[0] }}</div>
                <div class="certified-detail certified-detail-non-margin">{{ career[1] }}</div>
                <div class="certified-detail certified-detail-non-margin">~</div>
                <div class="certified-detail">{{ career[2] }}</div>
                <div class="certified-detail">{{ career[3] }}</div><div class="certified-detail">{{ career[4] }}</div>
                <div class="certified-detail">{{ career[5] }}</div><div class="certified-detail">{{ career[6] }}</div>
                <div class="certified-detail certified-detail-career-text" @click="onModal3(career[7])">
                  경력기술서
                </div>
                <div class="certified-detail certified-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                <div class="certified-detail certified-del-box" @click="delCareer('tmp', null, index2)">x</div>
              </div>
            </div>
          </div>
          <div class="resume-edit-career-input-box resume-edit-input-box">
            <div class="resume-edit-input-inner-box resume-edit-career-inner-box">
              <div class="inner-box career-name-input">
                <label for="">회사명</label>
                <input v-model="career.name" type="text" v-on:input="career.name = $event.target.value">
              </div>
              <div class="inner-box career-date-input">
                <label for="">근무기간</label>
                <input type="text" v-model='career.startDate' placeholder="YYYY . MM">
                <span>~</span>
                <input type="text" v-model='career.endDate' placeholder="YYYY . MM">
              </div>
              <div class="inner-box reson-input">
                <label for="career-reason">퇴직사유</label>
                <select v-model='career.reason' name="reson" id="career-reason">
                  <option disabled selected>선택</option>
                  <option>이직</option><option>학업</option><option>건강</option>
                  <option>해고</option><option>명퇴</option><option>만료</option>
                  <option>기타</option>
                </select>
              </div>
            </div>
            <div class="resume-edit-input-inner-box resume-edit-career-inner-box">
              <div class="inner-box career-department-input">
                <label for="">부서명</label>
                <input v-model="career.department" type="text" v-on:input="career.department = $event.target.value">
              </div>
              <div class="inner-box career-position-input">
                <label for="">직급</label>
                <input v-model="career.position" type="text" v-on:input="career.position = $event.target.value">
              </div>
              <div class="inner-box career-duties-input">
                <label for="">직무</label>
                <input v-model="career.duties" type="text" v-on:input="career.duties = $event.target.value">
              </div>
            </div>
            <div class="resume-edit-input-inner-box resume-edit-career-inner-text-box">
              <div class="resume-edit-career-text-head">
                <p>경력기술서 (500자)</p>
                <p>({{ career.text.length }}/500)</p>
              </div>
              <textarea name="" id="career-text" cols="30" rows="5"
              v-model="career.text" v-on:input="career.text = $event.target.value"></textarea>
            </div>
          </div>
          <div class="resume-edit-license-btn-box resume-edit-input-box">
            <div v-if="isCareer" class="resume-edit-license-btn  on-license-btn" @click="addCareer">인증하기</div>
            <div v-if="!isCareer" class="resume-edit-license-btn">인증하기</div>
          </div>
        </div>
      </div>

      <div class="resume-edit-box resume-edit-etc-box">
        <p>기타</p>
        <div class="resume-edit-license-content">
          <div class="resume-edit-license-certify-box">
            <p v-if="(certifiedEtc[0].length+certifiedEtc[1].length)===0">인증된 서류가 없습니다.</p>
            <div class='resume-edit-license-list-box' v-for='(etc, index) in certifiedEtc' :key='`etc-${index}`'>
              <div class="resume-edit-license-certified-list" v-if="(etc[0] || etc[1])">
                <div class="certified-detail certified-type">{{ etc[0] }}</div>
                <div class="certified-detail">{{ etc[1] }}</div><div class="certified-detail">{{ etc[2] }}</div>
                <div class="certified-detail certified-mark-box"><i class="far fa-check-circle"></i>인증됨</div>
                <div class="certified-detail certified-del-box" @click="delEtc(etc[0])">x</div>
              </div>
            </div>
          </div>
          <div class="resume-edit-license-school-box resume-edit-license-etc-box">
            <div class="resume-edit-license-school-btn veteran-btn" @click="onVeteran">보훈</div>
            <div class="resume-edit-license-school-btn disorder-btn" @click="onDisorder">장애</div>
          </div>

          <div v-if="isVeteran" class="resume-edit-license-etc-input-box resume-edit-input-box">
            <div class="resume-edit-input-inner-box">
              <div class="inner-box veteran-sort-input">
                <label for="veteran-sort">보훈구분</label>
                <select v-model='getData.veterans_classification' name="sort" id="veteran-sort">
                  <option disabled selected>선택</option>
                  <option>독립유공자</option><option>국가유공자</option><option>보훈보상대상자</option>
                  <option>참전유공자</option><option>5.18 민주유공자</option><option>특수임무유공자</option>
                  <option>제대군인</option>
                </select>
              </div>
              <div class="inner-box veteran-number-input">
                <label for="">보훈번호</label>
                <input v-model="getData.veterans_number" type="text" v-on:input="getData.veterans_number = $event.target.value">
              </div>
            </div>
          </div>
          <div v-if="isDisorder" class="resume-edit-license-etc-input-box resume-edit-input-box">
            <div class="resume-edit-input-inner-box">
              <div class="inner-box disorder-sort-input">
                <label for="disorder-sort">장애구분</label>
                <select v-model='getData.obstacle_classification' name="sort" id="disorder-sort">
                  <option disabled selected>선택</option>
                  <option>지체장애</option><option>뇌병변장애</option><option>시각장애</option>
                  <option>청각장애</option><option>언어장애</option><option>지적장애</option>
                  <option>정신장애</option><option>자폐성장애</option><option>신장장애</option>
                  <option>심장장애</option><option>호흡기장애</option><option>간장애</option>
                  <option>안면장애</option><option>간질장애</option><option>기타</option>
                </select>
              </div>
              <div class="inner-box disorder-rank-input">
                <label for="disorder-rank">등급</label>
                <select v-model='getData.obstacle_grade' name="rank" id="disorder-rank">
                  <option disabled selected>선택</option>
                  <option>1급</option><option>2급</option><option>3급</option>
                  <option>4급</option><option>5급</option><option>6급</option>
                  <option>7급</option>
                </select>
              </div>
            </div>
          </div>
          <div class="resume-edit-license-btn-box resume-edit-input-box">
            <div v-if="formVeteran" class="resume-edit-license-btn on-license-btn" @click="addEtc('veteran')">인증하기</div>
            <div v-if="formDisorder" class="resume-edit-license-btn on-license-btn" @click="addEtc('disorder')">인증하기</div>
            <div v-if="!isEtc" class="resume-edit-license-btn">인증하기</div>
          </div>
        </div>
      </div>
    </div>

    <SchoolSearch v-if="showModal" @close="showModal= false"/>
    <MajorSearch v-if="showModal2" @close="showModal2= false"/>
    <CareerModal v-if="showModal3" @close="showModal3= false"/>
    
  </div>
</template>

<script>
import { mapState,mapMutations,mapActions } from 'vuex';
import axios from 'axios';
import SchoolSearch from '../components/SchoolSearch.vue';
import MajorSearch from '../components/MajorSearch.vue';
import CareerModal from '../components/CareerModal.vue';
import '../components/css/resume-edit.css';
import Swal from 'sweetalert2';
import swal from 'sweetalert';

const SERVER_URL = 'https://j3b104.p.ssafy.io/api/'

export default {
  name: 'ResumeEdit',
  props: {
    first: {
      type: Boolean,
    },
    private_key: {
      type: Object,
    }
  },
  data() {
    return {
      showModal: false,
      showModal2: false,
      showModal3: false,
      profileImg: '',
      isSchool: false,
      isEtc: false,
      isLicense: false,
      isCareer: false,
      isCareerText1: [],
      isCareerText2: [],
      isLang: false,
      isVeteran: false,
      isDisorder: false,
      isHighSchool: false,
      isTecUniv: false,
      isUniv: false,
      isMaster: false,
      isDoctor: false,
      formHighSchool: false,
      formTecUniv: false,
      formUniv: false,
      formMaster: false,
      formDoctor: false,
      formVeteran: false,
      formDisorder: false,
      license: {
        name: '',
        institute: '',
        date: '',
      },
      career: {
        name: '',
        startDate: '',
        endDate: '',
        reason: '선택',
        department: '',
        position: '',
        duties: '',
        text: '',
      },
      lang: {
        sort: '선택',
        name: '',
        rank: '',
        date: '',
      },
      certifiedSchool: [[],[],[],[],[]],
      certifiedLicense: [],
      certifiedCareer: [],
      certifiedLang: [],
      certifiedEtc: [[],[]],
      getData: [],
      getLicense: [],
      delLicenseList: [],
      getLang: [],
      delLangList: [],
      getCareer: [],
      delCareerList: [],
      setData: [],
    }
  },
  components: {
    SchoolSearch,
    MajorSearch,
    CareerModal,
  },
  watch: {
    selectedSchool() {
      if (this.selectedSchoolType==='high') {this.getData.highschool_name = this.selectedSchool}
      else if (this.selectedSchoolType==='tecUniv') {this.getData.college_name = this.selectedSchool}
      else if (this.selectedSchoolType==='univ') {this.getData.university_name = this.selectedSchool}
      else if (this.selectedSchoolType==='master') {this.getData.master_name = this.selectedSchool}
      else if (this.selectedSchoolType==='doctor') {this.getData.doctor_name = this.selectedSchool}      
    },
    selectedMajor() {
      if (this.selectedMajorType2==='major') {
        if (this.selectedMajorType==='tecUniv') {this.getData.college_major = this.selectedMajor}
        else if (this.selectedMajorType==='univ') {this.getData.university_major = this.selectedMajor}
        else if (this.selectedMajorType==='master') {this.getData.master_major = this.selectedMajor}
        else if (this.selectedMajorType==='doctor') {this.getData.doctor_major = this.selectedMajor}      
      } else {
        if (this.selectedMajorType==='tecUniv') {this.getData.college_minor = this.selectedMajor}
        else if (this.selectedMajorType==='univ') {this.getData.university_minor = this.selectedMajor}
        else if (this.selectedMajorType==='master') {this.getData.master_minor = this.selectedMajor}
        else if (this.selectedMajorType==='doctor') {this.getData.doctor_minor = this.selectedMajor} 
      }
    },
    highSchool: {
      handler() {
        this.checkSchoolForm();
      }, deep:true
    },
    tecUniv: {
      handler() {
        this.checkSchoolForm();
      }, deep:true
    },
    univ: {
      handler() {
        this.checkSchoolForm();
      }, deep:true
    },
    master: {
      handler() {
        this.checkSchoolForm();
      }, deep:true
    },
    doctor: {
      handler() {
        this.checkSchoolForm();
      }, deep:true
    },
    license: {
      handler() {
        this.checkLicenseForm();
      }, deep:true
    },
    career: {
      handler() {
        this.checkCareerForm();
      }, deep:true
    },
    'career.text'() {
      this.setCareerText();
    },
    lang: {
      handler() {
        this.checkLangForm();
      }, deep:true
    },
    getData: {
      handler() {
        this.checkSchoolForm()
        this.checkEtc()
      }, deep:true
    },
  },
  created() {
    window.addEventListener('scroll', this.handleScroll)
  },
  mounted() {
    this.onHighSchool()
    this.onVeteran()
    setTimeout(() => {
      this.getResume()
    }, 1000);
    if (this.$cookies.isKey('auth-token')) {
      this.setIsLoggedIn(true);
      this.setToken(this.$cookies.get('auth-token'));
      this.setUserInfo();
    }
    else {
      this.setIsLoggedIn(false);
    }
    if (this.first === true) {
      swal(`warning\n`, `${this.private_key.result}\n\n1. 지갑 비밀키를 잃어버리지 마세요! 한 번 잃어버리면 복구 할 수 없습니다.\n2. 공유하지 마세요! 비밀키가 악위적인 사이트에 노출되면 당신의 자산이 유실될 수 있습니다.\n3. 백업을 만들어 두세요! 종이에 적어서 오프라인으로 관리하세요.`, "warning")
    }
  },
  computed: {
    ...mapState(['selectedSchool', 'selectedSchoolType', 'selectedMajor', 'selectedMajorType', 'selectedMajorType2', 'UserInfo']),
  },
  methods: {
    ...mapMutations(['setSchoolType', 'setSchoolName', 'setSchoolDetail', 'setSchoolType2', 'setMajorName', 'setMajorType', 'setMajorType2', 'setIsLoggedIn', 'setToken', 'setLoginPath', 'setUser', 'setCareerDetail']),
    ...mapActions(['setUserInfo']),
    setProfileImg() {
      const photoFile = document.getElementById("resume-edit-user-img-edit");
      this.getData.image = URL.createObjectURL(photoFile.files[0]);
      this.profileImg = photoFile.files[0]
    },
    onHighSchool() {
      const HIGH_SCHOOL = document.querySelector('.high-school-btn')
      const TEC_UNIV = document.querySelector('.tec-univ-btn')
      const UNIV = document.querySelector('.univ-btn')
      const MASTER = document.querySelector('.master-btn')
      const DOCTOR = document.querySelector('.doctor-btn')

      HIGH_SCHOOL.classList.add('on-school-btn')
      TEC_UNIV.classList.remove('on-school-btn')
      UNIV.classList.remove('on-school-btn')
      MASTER.classList.remove('on-school-btn')
      DOCTOR.classList.remove('on-school-btn')
      this.isHighSchool = true; this.isTecUniv = false; this.isUniv = false; 
      this.isMaster = false; this.isDoctor = false;
      this.checkSchoolForm()
    },
    onTecUniv() {
      const HIGH_SCHOOL = document.querySelector('.high-school-btn')
      const TEC_UNIV = document.querySelector('.tec-univ-btn')
      const UNIV = document.querySelector('.univ-btn')
      const MASTER = document.querySelector('.master-btn')
      const DOCTOR = document.querySelector('.doctor-btn')

      HIGH_SCHOOL.classList.remove('on-school-btn')
      TEC_UNIV.classList.add('on-school-btn')
      UNIV.classList.remove('on-school-btn')
      MASTER.classList.remove('on-school-btn')
      DOCTOR.classList.remove('on-school-btn')
      this.isHighSchool = false; this.isTecUniv = true; this.isUniv = false; 
      this.isMaster = false; this.isDoctor = false;
      this.checkSchoolForm()
    },
    onUniv() {
      const HIGH_SCHOOL = document.querySelector('.high-school-btn')
      const TEC_UNIV = document.querySelector('.tec-univ-btn')
      const UNIV = document.querySelector('.univ-btn')
      const MASTER = document.querySelector('.master-btn')
      const DOCTOR = document.querySelector('.doctor-btn')

      HIGH_SCHOOL.classList.remove('on-school-btn')
      TEC_UNIV.classList.remove('on-school-btn')
      UNIV.classList.add('on-school-btn')
      MASTER.classList.remove('on-school-btn')
      DOCTOR.classList.remove('on-school-btn')
      this.isHighSchool = false; this.isTecUniv = false; this.isUniv = true; 
      this.isMaster = false; this.isDoctor = false;
      this.checkSchoolForm()
    },
    onMaster() {
      const HIGH_SCHOOL = document.querySelector('.high-school-btn')
      const TEC_UNIV = document.querySelector('.tec-univ-btn')
      const UNIV = document.querySelector('.univ-btn')
      const MASTER = document.querySelector('.master-btn')
      const DOCTOR = document.querySelector('.doctor-btn')

      HIGH_SCHOOL.classList.remove('on-school-btn')
      TEC_UNIV.classList.remove('on-school-btn')
      UNIV.classList.remove('on-school-btn')
      MASTER.classList.add('on-school-btn')
      DOCTOR.classList.remove('on-school-btn')
      this.isHighSchool = false; this.isTecUniv = false; this.isUniv = false; 
      this.isMaster = true; this.isDoctor = false;
      this.checkSchoolForm()
    },
    onDoctor() {
      const HIGH_SCHOOL = document.querySelector('.high-school-btn')
      const TEC_UNIV = document.querySelector('.tec-univ-btn')
      const UNIV = document.querySelector('.univ-btn')
      const MASTER = document.querySelector('.master-btn')
      const DOCTOR = document.querySelector('.doctor-btn')

      HIGH_SCHOOL.classList.remove('on-school-btn')
      TEC_UNIV.classList.remove('on-school-btn')
      UNIV.classList.remove('on-school-btn')
      MASTER.classList.remove('on-school-btn')
      DOCTOR.classList.add('on-school-btn')
      this.isHighSchool = false; this.isTecUniv = false; this.isUniv = false; 
      this.isMaster = false; this.isDoctor = true;
      this.checkSchoolForm()
    },
    onVeteran() {
      const VETERAN = document.querySelector('.veteran-btn')
      const DISORDER = document.querySelector('.disorder-btn')

      VETERAN.classList.add('on-school-btn')
      DISORDER.classList.remove('on-school-btn')
      this.isVeteran = true; this.isDisorder = false;
      this.checkEtc()
    },
    onDisorder() {
      const VETERAN = document.querySelector('.veteran-btn')
      const DISORDER = document.querySelector('.disorder-btn')

      VETERAN.classList.remove('on-school-btn')
      DISORDER.classList.add('on-school-btn')
      this.isVeteran = false; this.isDisorder = true;
      this.checkEtc()
    },
    onModal(type, name, num, school) {
      this.setSchoolType(type);
      this.setSchoolName(name);
      this.setSchoolDetail(num);
      this.setSchoolType2(school);
      this.showModal = true;
    },
    onModal2(name, type, type2) {
      this.showModal2 = true;
      this.setMajorName(name);
      this.setMajorType(type);
      this.setMajorType2(type2);
    },
    onModal3(detail) {
      this.setCareerDetail(detail)
      this.showModal3 = true;
    },
    checkSchoolForm() {
      if ((this.getData.highschool_classification && this.getData.highschool_classification != '선택') && (this.getData.highschool_location && this.getData.highschool_location != '선택')
      && this.getData.highschool_name && this.getData.highschool_entrance_year && this.getData.highschool_graduation_year && this.isHighSchool) {
        this.formHighSchool = true; this.formTecUniv =  false; this.formUniv = false; this.formMaster = false; this.formDoctor = false; this.isSchool = true
      } else if ((this.getData.college_classification && this.getData.college_classification != '선택') && (this.getData.college_location && this.getData.college_location != '선택')
      && this.getData.college_name && this.getData.college_entrance_year && this.getData.college_graduation_year && this.getData.college_major
      && this.getData.college_grade && (this.getData.college_total && this.getData.college_total != '선택') && this.isTecUniv) {
        this.formHighSchool = false; this.formTecUniv =  true; this.formUniv = false; this.formMaster = false; this.formDoctor = false; this.isSchool = true
      } else if ((this.getData.university_classification && this.getData.university_classification != '선택') && (this.getData.university_location && this.getData.university_location != '선택')
      && this.getData.university_name && this.getData.university_entrance_year && this.getData.university_graduation_year && this.getData.university_major
      && this.getData.university_grade && (this.getData.university_total && this.getData.university_total != '선택') && this.isUniv){
        this.formHighSchool = false; this.formTecUniv =  false; this.formUniv = true; this.formMaster = false; this.formDoctor = false; this.isSchool = true
      } else if ((this.getData.master_classification && this.getData.master_classification != '선택') && (this.getData.master_location && this.getData.master_location != '선택')
      && this.getData.master_name && this.getData.master_entrance_year && this.getData.master_graduation_year && this.getData.master_major
      && this.getData.master_grade && (this.getData.master_total && this.getData.master_total != '선택') && this.isMaster){
        this.formHighSchool = false; this.formTecUniv =  false; this.formUniv = false; this.formMaster = true; this.formDoctor = false; this.isSchool = true
      } else if ((this.getData.doctor_classification && this.getData.doctor_classification != '선택') && (this.getData.doctor_location && this.getData.doctor_location != '선택')
      && this.getData.doctor_name && this.getData.doctor_entrance_year && this.getData.doctor_graduation_year && this.getData.doctor_major
      && this.getData.doctor_grade && (this.getData.doctor_total && this.getData.doctor_total != '선택') && this.isDoctor){
        this.formHighSchool = false; this.formTecUniv =  false; this.formUniv = false; this.formMaster = false; this.formDoctor = true; this.isSchool = true
      } else {
        this.formHighSchool = false; this.formTecUniv =  false; this.formUniv = false; this.formMaster = false; this.formDoctor = false; this.isSchool = false
      }
    },
    checkLicenseForm() {
      if (this.license.name && this.license.institute && this.license.date) {
        this.isLicense = true
      } else {
        this.isLicense = false
      }
    },
    checkCareerForm() {
      if (this.career.name && this.career.startDate && this.career.endDate
      && (this.career.reason && this.career.reason != '선택') && this.career.department
      && this.career.position && this.career.duties && this.career.text) {
        this.isCareer = true
      } else {
        this.isCareer = false
      }
    },
    checkLangForm() {
      if (this.lang.name && this.lang.rank && this.lang.date
      && (this.lang.sort && this.lang.sort != '선택')) {
        this.isLang = true
      } else {
        this.isLang = false
      }
    },
    checkEtc() {
      if (this.getData.veterans_number && (this.getData.veterans_classification && this.getData.veterans_classification != '선택') && this.isVeteran) {
        this.formVeteran = true; this.formDisorder = false; this.isEtc = true;
      } else if ((this.getData.obstacle_classification && this.getData.obstacle_classification != '선택') && (this.getData.obstacle_grade && this.getData.obstacle_grade != '선택') && this.isDisorder) {
        this.formDisorder = true; this.formVeteran = false; this.isEtc = true;
      } else {
        this.formVeteran = false; this.formDisorder = false; this.isEtc = false;
      }
    },
    checkgetDataForm() {
      // console.log('ss')
      // console.log(this.getData)
      // for (var key of data.keys()) {console.log(key);}
      // for (var value of this.getData.values()) {console.log(value);
      // this.cleanObj(this.getData)
    },
    addSchool(type) {
      this.goConfirm()
      if (type === 'high') {
        let ARR = ['고등학교']
        ARR.push(this.getData.highschool_name); ARR.push(this.getData.highschool_classification); ARR.push(this.getData.highschool_location);
        ARR.push(this.getData.highschool_entrance_year); ARR.push(this.getData.highschool_graduation_year);
        this.certifiedSchool[0] = ARR
        let tmp = this.getData.highschool_name; this.getData.highschool_name = ''; this.getData.highschool_name = tmp;
      } 
      
      else if (type === 'tecUniv'){
        let ARR = ['전문대학']
        ARR.push(this.getData.college_name); ARR.push(this.getData.college_classification); ARR.push(this.getData.college_location);
        ARR.push(this.getData.college_entrance_year); ARR.push(this.getData.college_graduation_year); ARR.push(this.getData.college_major);
        if (this.getData.college_minor) { ARR.push(this.getData.college_minor) } else { ARR.push('X') } ARR.push(this.getData.college_grade); ARR.push(this.getData.college_total)
        this.certifiedSchool[1] = ARR
        let tmp = this.getData.college_name; this.getData.college_name = ''; this.getData.college_name = tmp;
      } 
      
      else if (type === 'univ'){
        let ARR = ['대학교']
        ARR.push(this.getData.university_name); ARR.push(this.getData.university_classification); ARR.push(this.getData.university_location);
        ARR.push(this.getData.university_entrance_year); ARR.push(this.getData.university_graduation_year); ARR.push(this.getData.university_major);
        if (this.getData.university_minor) { ARR.push(this.getData.university_minor) } else { ARR.push('X') } ARR.push(this.getData.university_grade); ARR.push(this.getData.university_total)
        this.certifiedSchool[2] = ARR
        let tmp = this.getData.university_name; this.getData.university_name = ''; this.getData.university_name = tmp;
      } 
      
      else if (type === 'master'){
        let ARR = ['석사']
        ARR.push(this.getData.master_name); ARR.push(this.getData.master_classification); ARR.push(this.getData.master_location);
        ARR.push(this.getData.master_entrance_year); ARR.push(this.getData.master_graduation_year); ARR.push(this.getData.master_major);
        if (this.getData.master_minor) { ARR.push(this.getData.master_minor) } else { ARR.push('X') } ARR.push(this.getData.master_grade); ARR.push(this.getData.master_total)
        this.certifiedSchool[3] = ARR
        let tmp = this.getData.master_name; this.getData.master_name = ''; this.getData.master_name = tmp;
      } 
      
      else if (type === 'doctor'){
        let ARR = ['박사']
        ARR.push(this.getData.doctor_name); ARR.push(this.getData.doctor_classification); ARR.push(this.getData.doctor_location);
        ARR.push(this.getData.doctor_entrance_year); ARR.push(this.getData.doctor_graduation_year); ARR.push(this.getData.doctor_major);
        if (this.getData.doctor_minor) { ARR.push(this.getData.doctor_minor) } else { ARR.push('X') } ARR.push(this.getData.doctor_grade); ARR.push(this.getData.doctor_total)
        this.certifiedSchool[4] = ARR
        let tmp = this.getData.doctor_name; this.getData.doctor_name = ''; this.getData.doctor_name = tmp;
      }
    },
    addLicense() {
      this.goConfirm()
      let ARR = []
      ARR.push(this.license.name); ARR.push(this.license.institute); ARR.push(this.license.date);
      this.certifiedLicense.push(ARR)
      this.license.name = ''; this.license.institute = ''; this.license.date = '';
    },
    addCareer() {
      this.goConfirm()
      this.isCareerText2.push(false);
      let ARR = []
      ARR.push(this.career.name); ARR.push(this.career.startDate); ARR.push(this.career.endDate); ARR.push(this.career.reason); 
      ARR.push(this.career.department); ARR.push(this.career.position); ARR.push(this.career.duties); ARR.push(this.career.text)
      this.certifiedCareer.push(ARR);
      this.career.name = ''; this.career.startDate = ''; this.career.endDate = ''; this.career.reason = '선택'; 
      this.career.department = ''; this.career.position = ''; this.career.duties = ''; this.career.text = '';
    },
    addLang() {
      this.goConfirm()
      let ARR = []
      ARR.push(this.lang.sort); ARR.push(this.lang.name); ARR.push(this.lang.rank); ARR.push(this.lang.date); 
      this.certifiedLang.push(ARR)
      this.lang.sort = '선택'; this.lang.name = ''; this.lang.rank = ''; this.lang.date = ''; 
    },
    addEtc(type) {
      this.goConfirm()
      if (type === 'veteran') {
        let ARR = ['보훈']
        ARR.push(this.getData.veterans_classification); ARR.push(this.getData.veterans_number);
        this.certifiedEtc[0] = ARR
        let tmp = this.getData.veterans_classification; this.getData.veterans_classification = null; this.getData.veterans_classification = tmp; 
      } else if (type === 'disorder'){
        let ARR = ['장애']
        ARR.push(this.getData.obstacle_classification); ARR.push(this.getData.obstacle_grade); 
        this.certifiedEtc[1] = ARR
        let tmp = this.getData.obstacle_classification; this.getData.obstacle_classification = null; this.getData.obstacle_classification = tmp;
      }
    },
    delSchool(type) {
      if (type === '고등학교') {
        this.certifiedSchool[0] = []
        let tmp = this.isSchool; this.isSchool = null; this.isSchool = tmp;
        this.getData.highschool_name = ''; this.getData.highschool_classification = ''; this.getData.highschool_location = '';
        this.getData.highschool_entrance_year = ''; this.getData.highschool_graduation_year = '';  
      } else if (type === '전문대학') {
        this.certifiedSchool[1] = []
        let tmp = this.isSchool; this.isSchool = null; this.isSchool = tmp;
        this.getData.college_name = ''; this.getData.college_classification = ''; this.getData.college_location = '';
        this.getData.college_entrance_year = ''; this.getData.college_graduation_year = ''; this.getData.college_major = '';
        this.getData.college_minor = ''; this.getData.college_grade = undefined; this.getData.college_total = undefined;
      } else if (type === '대학교') {
        this.certifiedSchool[2] = []
        let tmp = this.isSchool; this.isSchool = null; this.isSchool = tmp;
        this.getData.university_name = ''; this.getData.university_classification = ''; this.getData.university_location = '';
        this.getData.university_entrance_year = ''; this.getData.university_graduation_year = ''; this.getData.university_major = '';
        this.getData.university_minor = ''; this.getData.university_grade = undefined; this.getData.university_total = undefined;
      } else if (type === '석사') {
        this.certifiedSchool[3] = []
        let tmp = this.isSchool; this.isSchool = null; this.isSchool = tmp;
        this.getData.master_name = ''; this.getData.master_classification = ''; this.getData.master_location = '';
        this.getData.master_entrance_year = ''; this.getData.master_graduation_year = ''; this.getData.master_major = '';
        this.getData.master_minor = ''; this.getData.master_grade = undefined; this.getData.master_total = undefined;
      } else if (type === '박사') {
        this.certifiedSchool[4] = []
        let tmp = this.isSchool; this.isSchool = null; this.isSchool = tmp;
        this.getData.doctor_name = ''; this.getData.doctor_classification = ''; this.getData.doctor_location = '';
        this.getData.doctor_entrance_year = ''; this.getData.doctor_graduation_year = ''; this.getData.doctor_major = '';
        this.getData.doctor_minor = ''; this.getData.doctor_grade = undefined; this.getData.doctor_total = undefined;
      }
    },
    delLicense(type, id, idx) {
      if (type === 'certified') {
        this.delLicenseList.push(id)
        this.getLicense[idx] = []
        let tmp = this.license.name; this.license.name = null; this.license.name = tmp;
      } else {
        this.certifiedLicense[idx] = []
        let tmp = this.license.name; this.license.name = null; this.license.name = tmp;
      }
    },
    delLang(type, id, idx) {
      if (type === 'certified') {
        this.delLangList.push(id)
        this.getLang[idx] = []
        let tmp = this.lang.name; this.lang.name = null; this.lang.name = tmp;
      } else {
        this.certifiedLang[idx] = []
        let tmp = this.lang.name; this.lang.name = null; this.lang.name = tmp;
      }
    },
    delCareer(type, id, idx) {
      if (type === 'certified') {
        this.delCareerList.push(id)
        this.getCareer[idx] = []
        let tmp = this.career.name; this.career.name = null; this.career.name = tmp;
      } else {
        this.certifiedCareer[idx] = []
        let tmp = this.career.name; this.career.name = null; this.career.name = tmp;
      }
    },
    delEtc(type) {
      if (type === '보훈') {
        this.certifiedEtc[0] = []
        let tmp = this.isVeteran; this.isVeteran = null; this.isVeteran = tmp;
        this.getData.veterans_classification = ''; this.getData.veterans_classification = '';
      } else if (type === '장애') {
        this.certifiedEtc[1] = []
        let tmp = this.isDisorder; this.isDisorder = null; this.isDisorder = tmp;
        this.getData.obstacle_classification = ''; this.getData.obstacle_grade = '';
      }
    },
    setCareerText() {
      if (this.career.text.length > 500) {
        this.career.text = this.career.text.substring(0,500)
      }
    },
    onCareerText1(text, idx) {
      if (text === 'on') {
        this.isCareerText1[idx] = true
      } else {
        this.isCareerText1[idx] = false
      }
    },
    onCareerText2(text, idx) {
      if (text === 'on') {
        this.isCareerText2[idx] = true
        this.isCareerText2[idx] = true
      } else {
        this.isCareerText2[idx] = false
      }
    },
    handleScroll() {
      const ORIGIN = -600
      let TOP = window.scrollY
      document.querySelector('.resume-edit-save-btn').style.bottom = (ORIGIN - TOP) + 'px';
    },
    getResume() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${SERVER_URL}articles/${this.UserInfo.id}/`, null, config)
      .then(res => {
        this.getData = res.data
        if(this.getData.image) {
          this.getData.image = 'https://j3b104.p.ssafy.io' + this.getData.image
        }
        this.sortSchool()
        this.sortEtc()
      })
      .catch(() => {})

      axios.get(`${SERVER_URL}articles/${this.UserInfo.id}/certificates/`, null, config)
      .then(res => {
        this.getLicense = res.data
      })
      .catch(() => {})

      axios.get(`${SERVER_URL}articles/${this.UserInfo.id}/languages/`, null, config)
      .then(res => {
        this.getLang = res.data
      })
      .catch(() => {})

      axios.get(`${SERVER_URL}articles/${this.UserInfo.id}/careers/`, null, config)
      .then(res => {
        for(let i=0; i<res.data.length; i++) {
          this.isCareerText1.push(false)
        }
        this.getCareer = res.data
      })
      .catch(() => {})
    },
    editResume() {
      this.editLicense()
      this.editLang()
      this.editCareer()
      this.cleanObj(this.getData)
      let data = new FormData();
      data.append('image', this.profileImg);
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      if (this.profileImg) {
        axios.put(`${SERVER_URL}articles/${this.UserInfo.id}/`, data, config)
        .then(() => {
        })
        .catch(() => {})
      }

      axios.put(`${SERVER_URL}articles/${this.UserInfo.id}/`, this.setData, config)
      .then(() => {
        this.$router.push('/resume').catch(()=>{})
      })
      .catch(() => {})
    },
    cleanObj(obj) {
      let propNames = Object.getOwnPropertyNames(obj);
      for (let i = 0; i < propNames.length; i++) {
        let propName = propNames[i];
        if (obj[propName] === null) {
          delete obj[propName];
        }
      delete obj['image']; delete obj['user']; delete obj['created_at']; delete obj['updated_at']
      this.setData = obj
     }
    },
    sortSchool() {
      if(this.getData.highschool_name) {
        let ARR = ['고등학교']
        ARR.push(this.getData.highschool_name); ARR.push(this.getData.highschool_classification); ARR.push(this.getData.highschool_location);
        ARR.push(this.getData.highschool_entrance_year); ARR.push(this.getData.highschool_graduation_year);
        this.certifiedSchool[0] = ARR
      }
      if(this.getData.college_name) {
        let ARR = ['전문대학']
        ARR.push(this.getData.college_name); ARR.push(this.getData.college_classification); ARR.push(this.getData.college_location);
        ARR.push(this.getData.college_entrance_year); ARR.push(this.getData.college_graduation_year); ARR.push(this.getData.college_major);
        if (this.getData.college_minor) { ARR.push(this.getData.college_minor) } else { ARR.push('X') } ARR.push(this.getData.college_grade); ARR.push(this.getData.college_total)
        this.certifiedSchool[1] = ARR
      }
      if(this.getData.university_name) {
        let ARR = ['대학교']
        ARR.push(this.getData.university_name); ARR.push(this.getData.university_classification); ARR.push(this.getData.university_location);
        ARR.push(this.getData.university_entrance_year); ARR.push(this.getData.university_graduation_year); ARR.push(this.getData.university_major);
        if (this.getData.university_minor) { ARR.push(this.getData.university_minor) } else { ARR.push('X') } ARR.push(this.getData.university_grade); ARR.push(this.getData.university_total)
        this.certifiedSchool[2] = ARR
      }
      if(this.getData.master_name) {
        let ARR = ['석사']
        ARR.push(this.getData.master_name); ARR.push(this.getData.master_classification); ARR.push(this.getData.master_location);
        ARR.push(this.getData.master_entrance_year); ARR.push(this.getData.master_graduation_year); ARR.push(this.getData.master_major);
        if (this.getData.master_minor) { ARR.push(this.getData.master_minor) } else { ARR.push('X') } ARR.push(this.getData.master_grade); ARR.push(this.getData.master_total)
        this.certifiedSchool[3] = ARR
      }
      if(this.getData.doctor_name) {
        let ARR = ['박사']
        ARR.push(this.getData.doctor_name); ARR.push(this.getData.doctor_classification); ARR.push(this.getData.doctor_location);
        ARR.push(this.getData.doctor_entrance_year); ARR.push(this.getData.doctor_graduation_year); ARR.push(this.getData.doctor_major);
        if (this.getData.doctor_minor) { ARR.push(this.getData.doctor_minor) } else { ARR.push('X') } ARR.push(this.getData.doctor_grade); ARR.push(this.getData.doctor_total)
        this.certifiedSchool[4] = ARR
      }
    },
    sortEtc() {
      if(this.getData.veterans_classification) {
        let ARR = ['보훈']
        ARR.push(this.getData.veterans_classification); ARR.push(this.getData.veterans_number);
        this.certifiedEtc[0] = ARR
      }
      if(this.getData.obstacle_classification) {
        let ARR = ['장애']
        ARR.push(this.getData.obstacle_classification); ARR.push(this.getData.obstacle_grade);
        this.certifiedEtc[1] = ARR
      }
    },
    editLicense() {
      for (let i=0; i<this.certifiedLicense.length; i++) {
        if (this.certifiedLicense[i].length > 0) {
          const config = {
            headers: {
              Authorization: `Token ${this.$cookies.get('auth-token')}`
            }
          }
          axios.post(`${SERVER_URL}articles/${this.UserInfo.id}/certificates/create/`, {
            article : this.UserInfo.id,
            name : this.certifiedLicense[i][0],
            publisher : this.certifiedLicense[i][1],
            date : this.certifiedLicense[i][2]
          }, config)
          .then(() => {
          })
          .catch(() => {})
        }
      }
      for (let i=0; i<this.delLicenseList; i++) {
        const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        // '<int:article_pk>/certificates/<int:certificate_pk>/'
        axios.delete(`${SERVER_URL}articles/${this.UserInfo.id}/certificates/${this.delLicenseList[i]}/`, null, config)
        .then(() => {
        })
        .catch(() => {})
      }
    },
    goConfirm() {
      const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
      axios.post(`${SERVER_URL}accounts/register/${this.UserInfo.id}/`, null, config)
        .then(() => {
        })
        .catch(() => {})
      let timerInterval
          Swal.fire({
            title: '잠시만 기다려주세요!',
            html: '기관이 자격증을 인증하고 있습니다',
            timer: 7000,
            timerProgressBar: true,
            showConfirmButton: false,
            willOpen: () => {
              Swal.showLoading()
              timerInterval = setInterval(() => {
                const content = Swal.getContent()
                if (content) {
                  const b = content.querySelector('b')
                  if (b) {
                    b.textContent = Swal.getTimerLeft()
                  }
                }
              }, 100)
            },
            onClose: () => {
              clearInterval(timerInterval)
            }
          }).then(() => {
            /* Read more about handling dismissals below */
          
            // <int:article_pk>/certificates/create
            // this.createCertificate()
            // this.createLang()
            // this.createCareer()
          })
          .catch(() => {})
      
    },
    editLang() {
      for (let i=0; i<this.certifiedLang.length; i++) {
        if (this.certifiedLang[i].length > 0) {
          const config = {
            headers: {
              Authorization: `Token ${this.$cookies.get('auth-token')}`
            }
          }
          axios.post(`${SERVER_URL}articles/${this.UserInfo.id}/languages/create/`, {
            article : this.UserInfo.id,
            classification: this.certifiedLang[i][0],
            name : this.certifiedLang[i][1],
            score : this.certifiedLang[i][2],
            date : this.certifiedLang[i][3]
          }, config)
          .then(() => {
          })
          .catch(() => {})
        }
      }
      for (let i=0; i<this.delLangList.length; i++) {
        const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        // '<int:article_pk>/certificates/<int:certificate_pk>/'
        axios.delete(`${SERVER_URL}articles/${this.UserInfo.id}/languages/${this.delLangList[i]}/`, null, config)
        .then(() => {
        })
        .catch(() => {})
      }
    },
    editCareer() {
      for (let i=0; i<this.certifiedCareer.length; i++) {
        if (this.certifiedCareer[i].length > 0) {
          const config = {
            headers: {
              Authorization: `Token ${this.$cookies.get('auth-token')}`
            }
          }
          axios.post(`${SERVER_URL}articles/${this.UserInfo.id}/careers/create/`, {
            article : this.UserInfo.id,
            name: this.certifiedCareer[i][0],
            start_term : this.certifiedCareer[i][1],
            end_term : this.certifiedCareer[i][2],
            retirement_reason : this.certifiedCareer[i][3],
            department: this.certifiedCareer[i][4],
            rank: this.certifiedCareer[i][5],
            duty: this.certifiedCareer[i][6],
            statement: this.certifiedCareer[i][7]
          }, config)
          .then(() => {
          })
          .catch(() => {})
        }
      }
      for (let i=0; i<this.delCareerList.length; i++) {
        const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        // '<int:article_pk>/certificates/<int:certificate_pk>/'
        axios.delete(`${SERVER_URL}articles/${this.UserInfo.id}/careers/${this.delCareerList[i]}/`, null, config)
        .then(() => {
        })
        .catch(() => {})
      }
    }
  },
  beforeDestroy () {
    window.removeEventListener('scroll', this.handleScroll)
  },
}
</script>