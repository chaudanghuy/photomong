import React, { useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { useNavigate } from 'react-router-dom';
import i18n from '../../translations/i18n';
import "../../css/Photo.css";
import continue_btn from '../../assets/Photo/Choose/continue_btn.png';
import continue_btn_click from '../../assets/Photo/Choose/continue_btn_click.png';
import photo_frame from '../../assets/Photo/Choose/photo_frame.png';

function Choose() {
     const { t } = useTranslation();
     const navigate = useNavigate();
     const [hoveredImage, setHoveredImage] = useState(null);

     const handleMouseEnter = (image) => {
          setHoveredImage(image);
     }

     const handleMouseLeave = () => {
          setHoveredImage(null);
     }

     return (
          <div className='photo-choose-container'>
               <div className="go-back" onClick={() => navigate("/photo")}></div>
               <div className="left-choose-container" style={{ backgroundImage: `url(${photo_frame})` }}></div>
               <div className="right-choose-container">
                    <div className="choose-line">
                         <div className="choose-image"></div>
                         <div className="choose-image"></div>
                         <div className="choose-image"></div>
                         <div className="choose-image"></div>
                    </div>
                    <div className="choose-line">
                         <div className="choose-image"></div>
                         <div className="choose-image"></div>
                         <div className="choose-image"></div>
                         <div className="choose-image"></div>
                    </div>
               </div>
               <div 
                    className="bottom_choose_container" 
                    style={{ backgroundImage: `url(${hoveredImage === continue_btn ? continue_btn_click : continue_btn})` }} 
                    onMouseEnter={() => handleMouseEnter(continue_btn)} 
                    onMouseLeave={handleMouseLeave}
                    onClick={() => navigate("/filter")}
               ></div>
          </div>
     );
}

export default Choose;